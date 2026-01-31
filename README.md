# 📈 Invest News Hub

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, streamlined Flask web application that aggregates real-time financial news from **50+ RSS feeds** across multiple categories including overall market news, tech sector, cryptocurrency, energy, real estate, forex, and international markets.

## Preview
![DEMO](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2w4YXQxcG5mZXZ0cnE3NHY5cjNxeWhkc2FoYndxYmtqaDU3cHpqayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/irOEqZS5j9Z58TfsKF/giphy.gif)

## 🌐 Live Demo
**[View Live Application →](https://invest-news-hub.onrender.com)**

A real-time financial news aggregator pulling from 50+ sources.
```

## ✨ Features

- **📰 50+ News Sources**: Aggregates from Yahoo Finance, WSJ, CNBC, Bloomberg, Reuters, TechCrunch, CoinDesk, and many more
- **🎯 Multi-Category Display**: Separate panels for different market sectors
- **🔍 Smart Ticker Detection**: Automatically extracts stock tickers from article titles
- **⏰ Relative Timestamps**: Shows "2h ago", "Yesterday", etc.
- **🎨 Modern UI**: Clean, responsive design that works on all devices
- **📊 Real-time Stats**: Article counts and tracking information at a glance
- **🔎 Powerful Search**: Search across all aggregated articles
- **📱 Fully Responsive**: Perfect experience on desktop, tablet, and mobile

## Search Showcase
![SEARCH](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3ZnY21zb2t1cnRuaG40cndlMGpicGk2bTZtYTR1bDN1d3hzY3YzcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZbVaVi33J7sqa7IzOl/giphy.gif)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AlexPGAO/invest-the-press.git
   cd invest-the-press
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```
   
   Or use the convenience script:
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## 📰 News Sources (50+ Feeds)

### Overall Market & Financial News (16 sources)
- Yahoo Finance
- Wall Street Journal
- CNBC
- Bloomberg
- Reuters Business
- MarketWatch
- Seeking Alpha
- The Motley Fool
- Investor's Business Daily
- Barron's
- Benzinga
- TheStreet
- Zero Hedge
- Abnormal Returns
- The Big Picture
- Calculated Risk

### Tech & Innovation (14 sources)
- TechCrunch
- The Verge
- Ars Technica
- Recode/Vox
- Wired
- Engadget
- VentureBeat
- ZDNet
- TechRadar
- CNET
- Hacker News
- MIT Technology Review
- Gizmodo
- TechRepublic

### Crypto & Blockchain (6 sources)
- CoinDesk
- Cointelegraph
- Cointelegraph Markets
- Bitcoin Magazine
- Decrypt
- The Block

### Energy & Commodities (3 sources)
- Oil Price
- Energy Voice
- Rigzone

### Real Estate (3 sources)
- Inman
- National Real Estate Investor
- Multi-Housing News

### Forex & Currency (3 sources)
- ForexLive
- DailyFX
- FXStreet

### International Markets (3 sources)
- South China Morning Post
- Nikkei Asia
- Economic Times India

### Video/Broadcast (2 sources)
- CNBC TV
- Bloomberg TV

## 🎨 Design Features

- **Modern Color Scheme**: Professional blue gradients
- **Card-Based Layout**: Clean shadowed cards with hover effects
- **Sticky Header**: Search always accessible
- **Responsive Grid**: 3 columns → 1 column on mobile
- **Smooth Animations**: Subtle transitions throughout

## 🔧 Configuration

### Change Tracking Period
Edit `app.py`:
```python
DAYS_TO_TRACK = 7  # Change to any number
```

### Add More RSS Feeds
Edit `app.py`:
```python
OVERALL_FEEDS = {
    'Your Source': 'https://your-feed-url.xml',
}
```

### Customize Colors
Edit `static/style.css`:
```css
:root {
  --primary-color: #2563eb;
  --bg-main: #f8fafc;
}
```

## 📊 API Endpoints

- **`/`** - Main page with news panels
- **`/search?q=query`** - Search results page
- **`/health`** - Health check endpoint (returns JSON)

## 🚦 Production Deployment

### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 app:app
```

### Deploy to Heroku
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### Deploy to Railway / Render
- Connect your GitHub repository
- Auto-detects Flask
- Deploy!

## 🛠️ Troubleshooting

**Articles not loading?**
→ Check internet connection, some feeds may be temporarily down

**Port 5000 busy?**
→ Edit `app.py`: `app.run(port=5001)`

**Too slow?**
→ Reduce `MAX_ENTRIES_PER_FEED` or implement caching

## 🔮 Coming Soon

- Option Hunter analytics panel
- Redis caching for faster loads
- User favorites and watchlists
- Email alerts for keywords
- Dark mode toggle
- Portfolio integration

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for **informational purposes only**. This is **NOT financial advice**. Always do your own research and consult with a qualified financial advisor before making investment decisions.

## 🙏 Acknowledgments

- Flask - The web framework
- Feedparser - RSS parsing
- All news organizations providing RSS feeds

---

**Built with Flask, Python, and ❤️**

For detailed documentation, see [QUICK_START.md](QUICK_START.md) and [CHANGES.md](CHANGES.md)
