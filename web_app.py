#!/usr/bin/env python3
"""
Stock Tracker Web App
A public-facing website that displays stock updates from multiple websites
"""

from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path
import threading
import time
from typing import Dict, List

app = Flask(__name__)

# Configuration
WEBSITES = [
    {"name": "Simply Mary", "url": "https://simplymary.co/"},
    {"name": "Hello Mary", "url": "https://shophellomary.com/"},
    {"name": "Crysp", "url": "https://crysp.co/"},
    {"name": "Southern Harvest Hemp", "url": "https://southernharvesthemp.com/"},
    {"name": "Quantum Exotics", "url": "https://www.quantumexotics.com/"}
]

CHECK_INTERVAL_MINUTES = 30
DATA_DIR = Path("web_tracker_data")
DATA_DIR.mkdir(exist_ok=True)

# Global data store
tracker_data = {
    "last_check": None,
    "websites": {},
    "recent_changes": []
}


class WebStockTracker:
    def __init__(self, websites: List[Dict]):
        self.websites = websites
        self.data_file = DATA_DIR / "tracker_state.json"
        self.load_state()
    
    def load_state(self):
        """Load saved state"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                tracker_data.update(data)
    
    def save_state(self):
        """Save current state"""
        with open(self.data_file, 'w') as f:
            json.dump(tracker_data, f, indent=2)
    
    def fetch_website(self, url: str) -> str:
        """Fetch website content"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_info(self, html: str) -> Dict:
        """Extract basic info from HTML"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Count potential product elements
        products = []
        product_selectors = [
            'div.product', 'article.product', '.product-item',
            '[class*="product-card"]', '[class*="product-grid"]'
        ]
        
        for selector in product_selectors:
            elements = soup.select(selector)
            if elements:
                for elem in elements:
                    name_elem = elem.select_one('h2, h3, h4, .product-title, .product-name')
                    if name_elem:
                        products.append(name_elem.get_text(strip=True))
        
        # Get page text for change detection
        page_text = soup.get_text(strip=True)
        
        return {
            'product_count': len(products),
            'products': products[:20],  # Store first 20 product names
            'content_hash': hashlib.md5(page_text.encode()).hexdigest(),
            'text_length': len(page_text)
        }
    
    def check_site(self, site: Dict) -> Dict:
        """Check a single site for updates"""
        url = site['url']
        name = site['name']
        
        html = self.fetch_website(url)
        if not html:
            return {
                'name': name,
                'url': url,
                'status': 'error',
                'error': 'Failed to fetch website'
            }
        
        current_info = self.extract_info(html)
        
        # Get previous data
        previous = tracker_data['websites'].get(url, {})
        
        # Detect changes
        changes = []
        if previous:
            if previous.get('content_hash') != current_info['content_hash']:
                changes.append('Content updated')
            
            count_diff = current_info['product_count'] - previous.get('product_count', 0)
            if count_diff > 0:
                changes.append(f'{count_diff} new product(s) added')
            elif count_diff < 0:
                changes.append(f'{abs(count_diff)} product(s) removed')
        
        result = {
            'name': name,
            'url': url,
            'status': 'ok',
            'product_count': current_info['product_count'],
            'products': current_info['products'],
            'last_checked': datetime.now().isoformat(),
            'changes': changes,
            'has_changes': len(changes) > 0
        }
        
        # Update tracker data
        tracker_data['websites'][url] = {
            'name': name,
            'url': url,
            'product_count': current_info['product_count'],
            'products': current_info['products'],
            'content_hash': current_info['content_hash'],
            'last_checked': result['last_checked'],
            'status': 'ok'
        }
        
        # Add to recent changes if there are any
        if changes:
            change_entry = {
                'name': name,
                'url': url,
                'timestamp': result['last_checked'],
                'changes': changes
            }
            tracker_data['recent_changes'].insert(0, change_entry)
            # Keep only last 50 changes
            tracker_data['recent_changes'] = tracker_data['recent_changes'][:50]
        
        return result
    
    def check_all_sites(self):
        """Check all websites"""
        print(f"Starting check at {datetime.now()}")
        
        for site in self.websites:
            self.check_site(site)
            time.sleep(2)  # Be polite
        
        tracker_data['last_check'] = datetime.now().isoformat()
        self.save_state()
        
        print(f"Check complete at {datetime.now()}")
    
    def run_background_checks(self, interval_minutes: int):
        """Run checks in background thread"""
        while True:
            try:
                self.check_all_sites()
            except Exception as e:
                print(f"Error in background check: {e}")
            
            time.sleep(interval_minutes * 60)


# Initialize tracker
tracker = WebStockTracker(WEBSITES)

# Start background checking
def start_background_tracker():
    # Do initial check
    tracker.check_all_sites()
    # Start continuous checks
    thread = threading.Thread(
        target=tracker.run_background_checks,
        args=(CHECK_INTERVAL_MINUTES,),
        daemon=True
    )
    thread.start()


# Web routes
@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')


@app.route('/api/status')
def api_status():
    """API endpoint for current status"""
    return jsonify(tracker_data)


@app.route('/api/refresh')
def api_refresh():
    """Trigger a manual refresh"""
    thread = threading.Thread(target=tracker.check_all_sites, daemon=True)
    thread.start()
    return jsonify({"status": "refresh_started"})


if __name__ == '__main__':
    # Start background tracker
    start_background_tracker()
    
    # Run web server
    # Use 0.0.0.0 to make it accessible from other devices
    # Use port 5000 (can be changed)
    print("Starting Stock Tracker Web Server...")
    print("Visit http://localhost:5000 in your browser")
    app.run(host='0.0.0.0', port=5000, debug=False)
