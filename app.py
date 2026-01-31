import feedparser
from flask import Flask, render_template, request
import re
from datetime import datetime, timedelta
import pytz
import requests

app = Flask(__name__)

# Grouped feeds
OVERALL_FEEDS = {
    'Yahoo Finance': 'https://finance.yahoo.com/news/rssindex',
    'Wall Street Journal': 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
    'Bloomberg': 'https://feeds.bloomberg.com/markets/news.rss',
    'MarketWatch': 'https://feeds.marketwatch.com/marketwatch/topstories/',
    'Seeking Alpha': 'https://seekingalpha.com/feed.xml',
    'The Motley Fool': 'https://www.fool.com/feeds/index.aspx',
    'Investor\'s Business Daily': 'https://www.investors.com/feed/',
    'Financial Times': 'https://www.ft.com/?format=rss',
    'Benzinga': 'https://www.benzinga.com/feed',
    'CNBC': 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15839069',
}

TECH_FEEDS = {
    'TechCrunch': 'http://feeds.feedburner.com/TechCrunch/',
    'The Verge': 'https://www.theverge.com/rss/index.xml',
    'Ars Technica': 'http://feeds.arstechnica.com/arstechnica/index',
    'Recode/Vox': 'http://www.vox.com/rss/index.xml',
    'Wired': 'https://www.wired.com/feed/rss',
    'Engadget': 'https://www.engadget.com/rss.xml',
    'VentureBeat': 'https://venturebeat.com/feed/',
    'ZDNet': 'https://www.zdnet.com/news/rss.xml',
    'TechRadar': 'https://www.techradar.com/rss',
    'CNET': 'https://www.cnet.com/rss/news/',
    'Hacker News': 'https://news.ycombinator.com/rss',
    'MIT Technology Review': 'https://www.technologyreview.com/feed/',
    'Gizmodo': 'https://gizmodo.com/rss',
    'TechRepublic': 'https://www.techrepublic.com/rssfeeds/articles/',
}

# Configuration
EST = pytz.timezone('US/Eastern')
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) InvestThePress/1.0"
REQUEST_TIMEOUT = 6
MAX_ENTRIES_PER_FEED = 50
DAYS_TO_TRACK = 7

def extract_ticker(title: str) -> str | None:
    """Extract stock ticker from article title using multiple patterns."""
    if not title:
        return None
    
    # Pattern 1: Ticker in parentheses (AAPL)
    m = re.search(r"\(([A-Z]{1,5})\)", title)
    if m:
        return m.group(1)
    
    # Pattern 2: Exchange prefix (NASDAQ: AAPL)
    m = re.search(r"\b(?:NASDAQ|NYSE|AMEX|LSE|TSX)[:\s]+([A-Z\.-]{1,6})\b", title)
    if m:
        return m.group(1).replace('.', '-').upper()
    
    # Pattern 3: Dollar sign prefix ($AAPL)
    m = re.search(r"\$([A-Z]{1,5})\b", title)
    if m:
        return m.group(1).upper()
    
    # Pattern 4: Explicit ticker/symbol mention
    m = re.search(r"\b(?:ticker|symbol)[:\s]+([A-Z]{1,5})\b", title, flags=re.IGNORECASE)
    if m:
        return m.group(1).upper()
    
    # Pattern 5: Standalone uppercase words (filtered)
    tokens = re.findall(r"\b[A-Z]{1,5}\b", title)
    common = {"THE", "AND", "FOR", "WITH", "WALL", "STREET", "NEWS", "NEW", "YORK", "US", "UK"}
    for t in tokens:
        if t not in common:
            return t
    
    return None

def format_date(published_dt):
    """Format datetime for display."""
    if not published_dt:
        return None
    
    now = datetime.now(EST)
    diff = now - published_dt
    
    if diff.days == 0:
        hours = diff.seconds // 3600
        if hours == 0:
            minutes = diff.seconds // 60
            return f"{minutes}m ago" if minutes > 0 else "Just now"
        return f"{hours}h ago"
    elif diff.days == 1:
        return "Yesterday"
    elif diff.days < 7:
        return f"{diff.days}d ago"
    else:
        return published_dt.strftime("%b %d")

def fetch_grouped_articles():
    """Fetch, filter (last N days), and return two lists: overall, tech."""
    now = datetime.now(EST)
    cutoff = now - timedelta(days=DAYS_TO_TRACK)

    def fetch_from(feeds: dict, group_name: str):
        rows = []
        for source, url in feeds.items():
            try:
                resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=REQUEST_TIMEOUT)
                resp.raise_for_status()
                parsed = feedparser.parse(resp.content)
            except Exception as ex:
                print(f"[{group_name}/{source}] Error fetching feed: {ex}")
                continue

            for e in parsed.entries[:MAX_ENTRIES_PER_FEED]:
                title = getattr(e, 'title', '') or ''
                link = getattr(e, 'link', None)
                
                if not link or not title:
                    continue

                # Parse published date
                pp = getattr(e, 'published_parsed', None)
                published_dt_est = None
                
                if pp:
                    try:
                        published_dt_est = datetime(*pp[:6], tzinfo=pytz.UTC).astimezone(EST)
                        # Skip articles older than cutoff
                        if published_dt_est < cutoff:
                            continue
                    except Exception:
                        published_dt_est = None

                ticker = extract_ticker(title)
                
                rows.append({
                    'group': group_name,
                    'source': source,
                    'title': title,
                    'link': link,
                    'published_parsed': pp,
                    'published_dt_est': published_dt_est,
                    'published_str': format_date(published_dt_est),
                    'ticker': ticker,
                    'yahoo_url': f"https://finance.yahoo.com/quote/{ticker}" if ticker else None,
                })
        
        if not rows:
            return rows
        
        # Sort by date (newest first)
        rows.sort(key=lambda x: x['published_dt_est'].timestamp() if x['published_dt_est'] else 0, reverse=True)
        return rows

    overall = fetch_from(OVERALL_FEEDS, 'overall')
    tech = fetch_from(TECH_FEEDS, 'tech')
    
    return overall, tech

@app.route('/')
def index():
    """Main page displaying overall market and tech news."""
    overall_articles, tech_articles = fetch_grouped_articles()
    
    return render_template(
        'index.html',
        overall_articles=overall_articles,
        tech_articles=tech_articles,
        overall_count=len(overall_articles),
        tech_count=len(tech_articles),
    )

@app.route('/search')
def search():
    """Search across all articles."""
    query = (request.args.get('q') or '').strip().lower()
    
    overall_articles, tech_articles = fetch_grouped_articles()
    all_articles = (overall_articles or []) + (tech_articles or [])
    
    if query:
        all_articles = [a for a in all_articles if query in (a['title'] or '').lower()]
    
    return render_template(
        'search_results.html',
        articles=all_articles,
        query=query
    )

@app.route('/health')
def health():
    """Health check endpoint."""
    try:
        overall, tech = fetch_grouped_articles()
        return {
            "status": "ok",
            "overall_count": len(overall),
            "tech_count": len(tech),
            "timestamp": datetime.now(EST).isoformat()
        }, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
