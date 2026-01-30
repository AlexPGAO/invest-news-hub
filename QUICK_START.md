# 🚀 QUICK START GUIDE - Invest the Press

## Get Running in 3 Steps

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the App
```bash
python app.py
```

Or use the startup script:
```bash
./start.sh
```

### 3️⃣ Open in Browser
```
http://localhost:5000
```

**That's it!** 🎉

---

## 📰 What You Get

### 50+ News Sources Across 8 Categories

#### 💼 Overall Market (16 sources)
Yahoo Finance • WSJ • CNBC • Bloomberg • Reuters • MarketWatch • Seeking Alpha • Motley Fool • IBD • Barron's • Benzinga • TheStreet • Zero Hedge • Abnormal Returns • The Big Picture • Calculated Risk

#### 💻 Tech (14 sources)
TechCrunch • The Verge • Ars Technica • Vox • Wired • Engadget • VentureBeat • ZDNet • TechRadar • CNET • Hacker News • MIT Tech Review • Gizmodo • TechRepublic

#### 🪙 Crypto (6 sources)
CoinDesk • Cointelegraph • Bitcoin Magazine • Decrypt • The Block

#### ⚡ Energy (3 sources)
Oil Price • Energy Voice • Rigzone

#### 🏠 Real Estate (3 sources)
Inman • NREI • Multi-Housing News

#### 💱 Forex (3 sources)
ForexLive • DailyFX • FXStreet

#### 🌏 International (3 sources)
SCMP • Nikkei Asia • Economic Times India

#### 📺 Video/Broadcast (2 sources)
CNBC TV • Bloomberg TV

---

## 🎨 Features at a Glance

✅ **Real-time news** from 50+ sources  
✅ **Smart ticker extraction** (AAPL, TSLA, etc.)  
✅ **Relative timestamps** ("2h ago", "Yesterday")  
✅ **Source attribution** for every article  
✅ **Powerful search** across all feeds  
✅ **Mobile responsive** design  
✅ **Direct Yahoo Finance links** for tickers  
✅ **7-day tracking** period  

---

## 📁 File Structure

```
invest-the-press/
├── app.py                    # Main Flask app
├── requirements.txt          # Dependencies
├── start.sh                  # Startup script
├── templates/
│   ├── base.html            # Header/footer
│   ├── index.html           # Main page
│   └── search_results.html  # Search page
└── static/
    └── style.css            # Styles
```

---

## ⚙️ Quick Customization

### Change Tracking Period
**File:** `app.py` (around line 95)
```python
DAYS_TO_TRACK = 7  # Change to 3, 14, 30, etc.
```

### Add Your Own RSS Feed
**File:** `app.py` (lines 11-80)
```python
OVERALL_FEEDS = {
    'My Custom Source': 'https://your-feed-url.xml',
}
```

### Change Colors
**File:** `static/style.css` (lines 16-28)
```css
:root {
  --primary-color: #2563eb;  /* Main blue */
  --bg-main: #f8fafc;        /* Background */
}
```

---

## 🔧 Common Commands

### Start the app
```bash
python app.py
```

### Check if everything works
```bash
python -c "import app; print('✅ All good!')"
```

### Test health endpoint
```bash
curl http://localhost:5000/health
```

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 5000 busy | Change port: `app.run(port=5001)` |
| No articles showing | Check internet, refresh page |
| Slow loading | Reduce `MAX_ENTRIES_PER_FEED` |
| Import errors | Run `pip install -r requirements.txt` |

---

## 📊 Understanding the Interface

### Stats Bar (Top)
Shows:
- Overall Market article count
- Tech article count  
- Tracking period (7 days)

### Main Panels
- **Overall Market**: General financial news
- **Tech**: Technology sector news
- **Coming Soon**: Option Hunter feature preview

### Each Article Shows
- **Title** (clickable to source)
- **Source** (e.g., "Bloomberg")
- **Time** (e.g., "2h ago")
- **Ticker** (if detected, e.g., "AAPL")

### Search Function
- Located in header
- Searches ALL articles
- Shows source and category
- Preserves metadata


## 📚 More Information

- **Full docs**: See `README.md`
- **Changelog**: See `CHANGES.md`
- **License**: See `LICENSE`

---

## 💡 Pro Tips

1. **Bookmark it** - Access your news dashboard quickly
2. **Use search** - Find specific tickers or companies fast
3. **Check daily** - Articles update on every page load
4. **Mobile works great** - Use on your phone
5. **Click tickers** - Direct link to Yahoo Finance charts

---

## 🎯 What Makes This Special?

| Feature | Details |
|---------|---------|
| **Sources** | 50+ curated RSS feeds |
| **Categories** | 8 different market sectors |
| **Updates** | Real-time on every load |
| **Design** | Modern, professional UI |
| **Mobile** | Fully responsive |
| **Search** | Across ALL sources |
| **Free** | 100% open source |

---

## ⚡ Performance Notes

- Articles fetch on page load (no background updates)
- Each feed limited to 50 articles max
- 6-second timeout per feed
- 7-day lookback period
- No database required
- No API keys needed

---

## 🔮 Coming Features

- 🎯 Option Hunter panel
- 💾 Redis caching
- ⭐ User favorites
- 📧 Email alerts
- 🌙 Dark mode
- 📱 Mobile app

---

## 🤝 Need Help?

- Check `README.md` for detailed docs
- Look at `CHANGES.md` for what's new
- Create GitHub issue for bugs
- Read the code comments

---

**Ready to start?** Just run `python app.py` and visit `http://localhost:5000`

**Questions?** Everything is documented in the code and README.

**Enjoy your streamlined financial news aggregator!** 📈✨
