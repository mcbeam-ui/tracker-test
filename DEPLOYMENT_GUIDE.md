# 🌐 Stock Tracker Web App - Deployment Guide

## What You're Getting

A beautiful, public-facing website that automatically tracks stock updates from your 5 websites and displays them in real-time. Anyone can visit your site to see the latest stock information!

---

## 🚀 EASIEST WAY: Deploy to Cloud (No Coding Required!)

I recommend using **Render.com** - it's FREE and super easy!

### Step-by-Step for Render.com:

#### 1. **Create a Free Render Account**
   - Go to https://render.com
   - Click "Get Started" 
   - Sign up with GitHub (easiest) or email

#### 2. **Upload Your Files to GitHub**
   - Go to https://github.com
   - Sign up/login
   - Click the "+" in top right → "New repository"
   - Name it "stock-tracker" (or anything you want)
   - Click "creating a new file"
   - Upload these files:
     - `web_app.py`
     - `requirements_web.txt` (rename to `requirements.txt`)
     - `templates/index.html` (create `templates` folder first)

#### 3. **Deploy on Render**
   - Back on Render.com, click "New +"
   - Select "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: stock-tracker (or your choice)
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn web_app:app`
     - **Plan**: Free
   - Click "Create Web Service"

#### 4. **Wait 5-10 Minutes**
   - Render will build and deploy your app
   - You'll get a URL like: `https://stock-tracker-xxxx.onrender.com`
   - Share this URL with anyone!

---

## 🏠 ALTERNATIVE: Run on Your Own Computer

Perfect if you just want to test locally first.

### For Windows:

1. **Install Python**
   - Download from https://python.org
   - Check "Add Python to PATH" during installation

2. **Open Command Prompt** (search "cmd")

3. **Navigate to your folder**:
   ```
   cd C:\path\to\your\files
   ```

4. **Install requirements**:
   ```
   pip install flask requests beautifulsoup4 lxml
   ```

5. **Run the app**:
   ```
   python web_app.py
   ```

6. **Open browser** to `http://localhost:5000`

### For Mac/Linux:

1. **Open Terminal**

2. **Navigate to your folder**:
   ```bash
   cd /path/to/your/files
   ```

3. **Install requirements**:
   ```bash
   pip3 install flask requests beautifulsoup4 lxml
   ```

4. **Run the app**:
   ```bash
   python3 web_app.py
   ```

5. **Open browser** to `http://localhost:5000`

---

## 🎯 OTHER EASY HOSTING OPTIONS

### Option 1: PythonAnywhere (Free Tier)
1. Sign up at https://pythonanywhere.com
2. Upload files via "Files" tab
3. Create new web app (Flask)
4. Configure WSGI file
5. Get URL: `https://yourusername.pythonanywhere.com`

**Pros**: Very beginner friendly
**Cons**: Free tier sleeps after inactivity

### Option 2: Railway.app
1. Sign up at https://railway.app
2. "New Project" → "Deploy from GitHub"
3. Connect repository
4. Auto-deploys!

**Pros**: Super fast setup
**Cons**: $5/month after trial

### Option 3: Heroku
1. Sign up at https://heroku.com
2. Install Heroku CLI
3. Deploy with: `git push heroku main`

**Pros**: Very popular, lots of tutorials
**Cons**: No free tier anymore ($7/month minimum)

---

## ⚙️ Customization

### Change Check Frequency

Edit `web_app.py`, find this line:
```python
CHECK_INTERVAL_MINUTES = 30
```
Change to:
```python
CHECK_INTERVAL_MINUTES = 15  # Check every 15 minutes
CHECK_INTERVAL_MINUTES = 60  # Check every hour
```

### Add More Websites

In `web_app.py`, find the `WEBSITES` list:
```python
WEBSITES = [
    {"name": "Simply Mary", "url": "https://simplymary.co/"},
    # Add new ones here:
    {"name": "New Site", "url": "https://newsite.com/"},
]
```

### Change Colors/Style

The entire design is in `templates/index.html` inside the `<style>` tag. 
Change colors by finding and replacing hex codes like `#667eea` with your preferred colors.

---

## 📱 Features Your Site Will Have

✅ **Auto-refreshing dashboard** - Updates every 30 seconds  
✅ **Product counts** - Shows how many products each site has  
✅ **Change detection** - Highlights when stock updates  
✅ **Change history** - Shows recent additions/removals  
✅ **Mobile responsive** - Works on phones and tablets  
✅ **Manual refresh button** - Force immediate check  
✅ **Beautiful modern design** - Professional purple gradient theme  

---

## 🔍 Troubleshooting

### "No changes detected yet"
- This is normal on first run
- Wait 30 minutes for the first automated check
- Or click "Refresh Now" button

### "Failed to fetch website"
- Some sites block automated requests
- The bot will keep trying
- Check `web_tracker_data/tracker_state.json` for details

### Site not loading
- Check that Python is running
- Make sure port 5000 isn't already in use
- Look for error messages in terminal

### Changes not showing
- The bot checks every 30 minutes
- First run creates a baseline (no changes reported)
- Real changes will show on subsequent checks

---

## 💡 Tips for Success

1. **Start with Render.com** - Easiest for beginners
2. **Test locally first** - Make sure it works on your computer
3. **Check the logs** - Render and other platforms show error logs
4. **Be patient** - First deploy takes 5-10 minutes
5. **Share your URL** - Once deployed, anyone can access it!

---

## 🆘 Need Help?

If you get stuck:
1. Check the error message in the terminal/logs
2. Google the error message
3. Check if Python and all packages are installed
4. Make sure all files are in the right folders
5. Try restarting the application

---

## 📊 What Happens After Deployment

Once live, your site will:
- Check all 5 websites automatically every 30 minutes
- Save snapshots to detect changes
- Display updates in real-time on the dashboard
- Keep a history of all changes
- Run 24/7 without you doing anything!

---

## 🎉 You're All Set!

Your stock tracker will now run automatically and be accessible to anyone with the URL. The site updates itself, tracks changes, and looks professional!

**No coding experience needed - just follow the steps above!** 🚀
