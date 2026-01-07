# 🌿 Stock Tracker Web Dashboard

A beautiful, public-facing website that automatically monitors 5 hemp/cannabis product websites for stock updates.

![Dashboard](https://img.shields.io/badge/Status-Live-success)
![Auto%20Update](https://img.shields.io/badge/Auto%20Update-30%20min-blue)
![Python](https://img.shields.io/badge/Python-3.7+-blue)

---

## 🎯 What This Does

- **Monitors 5 websites** automatically every 30 minutes
- **Detects changes** in stock/products
- **Beautiful dashboard** anyone can view
- **Change history** showing what's new or removed
- **Real-time updates** - dashboard refreshes automatically
- **Mobile friendly** - works on phones and tablets

---

## 🚀 Quick Start (3 Steps)

### For Windows:
1. Double-click `START_WINDOWS.bat`
2. Wait for installation (first time only)
3. Open browser to `http://localhost:5000`

### For Mac/Linux:
1. Double-click `START_MAC_LINUX.sh` (or run `./START_MAC_LINUX.sh` in terminal)
2. Wait for installation (first time only)
3. Open browser to `http://localhost:5000`

**That's it!** Your stock tracker website is now running.

---

## 🌐 Make It Public (Deploy Online)

Want anyone on the internet to access your tracker? See **DEPLOYMENT_GUIDE.md** for:

- ✅ **Render.com** (FREE, easiest, recommended)
- ✅ **PythonAnywhere** (FREE)
- ✅ **Railway.app** ($5/month after trial)
- ✅ **Your own server** (for advanced users)

**No coding needed** - just follow the step-by-step guide!

---

## 📊 Dashboard Features

### Status Bar
- Last check time
- Number of websites tracked  
- Auto-refresh interval
- Manual refresh button

### Website Cards
- Current product count
- Last check time
- Sample products
- Status indicator (Active/Error)
- Change notifications (highlighted in green)

### Recent Changes
- What changed
- When it changed
- Which website changed
- Details (products added/removed)

---

## ⚙️ Configuration

### Change Check Frequency

Edit `web_app.py`, line 23:
```python
CHECK_INTERVAL_MINUTES = 30  # Change this number
```

Options:
- `15` = Every 15 minutes
- `30` = Every 30 minutes (default)
- `60` = Every hour
- `120` = Every 2 hours

### Add More Websites

Edit `web_app.py`, lines 15-21:
```python
WEBSITES = [
    {"name": "Your Site Name", "url": "https://yoursite.com/"},
    # Add more here
]
```

### Customize Appearance

Edit `templates/index.html` to change:
- Colors (search for `#667eea` and `#764ba2`)
- Layout
- Text and labels
- Fonts

---

## 📁 File Structure

```
stock-tracker/
├── web_app.py              # Main application
├── requirements_web.txt    # Python dependencies
├── templates/
│   └── index.html         # Website template
├── START_WINDOWS.bat      # Windows launcher
├── START_MAC_LINUX.sh     # Mac/Linux launcher
├── DEPLOYMENT_GUIDE.md    # How to deploy online
└── web_tracker_data/      # Created automatically
    ├── tracker_state.json # Saved data
    └── site_*.json        # Website snapshots
```

---

## 🔧 Requirements

- Python 3.7 or higher
- Internet connection
- Web browser

Auto-installed packages:
- Flask (web framework)
- Requests (fetch websites)
- BeautifulSoup4 (parse HTML)
- lxml (HTML parser)

---

## 💡 How It Works

1. **Background Thread**: Checks all 5 websites every 30 minutes
2. **Data Storage**: Saves snapshots to detect changes
3. **Change Detection**: Compares new data vs. previous snapshots
4. **Web Dashboard**: Displays everything in real-time
5. **Auto-refresh**: Dashboard updates every 30 seconds

---

## 🐛 Troubleshooting

### "Failed to fetch website"
- **Cause**: Website blocking automated requests or down
- **Solution**: Bot will retry next cycle, this is normal

### Changes not showing
- **First run**: Creates baseline, no changes yet
- **Wait**: Give it 30+ minutes for first real check
- **Manual refresh**: Click the "Refresh Now" button

### Port already in use
- **Error**: Something else is using port 5000
- **Solution**: Close other programs or change port in `web_app.py`:
  ```python
  app.run(host='0.0.0.0', port=5001)  # Use port 5001 instead
  ```

### Can't install requirements
- **Windows**: Make sure Python is in PATH
- **Mac**: Use `pip3` instead of `pip`
- **Linux**: May need `sudo pip3 install ...`

---

## 🎨 Customization Ideas

- Change the color scheme (purple gradient can be any color)
- Add email notifications when changes detected
- Add more detailed product information
- Create price tracking
- Add charts/graphs of product count over time
- Filter by product category
- Export change history to CSV

---

## 📈 Monitoring Websites

Currently tracking:
1. **Simply Mary** - https://simplymary.co/
2. **Hello Mary** - https://shophellomary.com/
3. **Crysp** - https://crysp.co/
4. **Southern Harvest Hemp** - https://southernharvesthemp.com/
5. **Quantum Exotics** - https://www.quantumexotics.com/

---

## 🎉 You're Done!

Your stock tracker is:
- ✅ Running automatically
- ✅ Checking websites every 30 minutes  
- ✅ Detecting all changes
- ✅ Displaying beautiful dashboard
- ✅ Ready to share with others!

**Next step**: Check out DEPLOYMENT_GUIDE.md to make it public online! 🚀
