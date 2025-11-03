# Quick Start Guide

Get your NABII Impact Investment Dashboard running in 3 simple steps!

## 🚀 Quick Launch (Easiest Method)

```bash
python launch.py
```

This will:
1. Start a local web server
2. Automatically open the dashboard in your browser
3. Display all 8 interactive visualizations

**That's it!** Your dashboard is now running at `http://localhost:8000`

---

## 📋 Step-by-Step Setup

### Step 1: Install Dependencies

```bash
pip install pandas openpyxl
```

### Step 2: Process the Data

```bash
python process_data.py
```

**Expected Output:**
```
Loading data from Excel...
Total records: 128
Anonymized deals (excluded from individual display): 10
Deals with disclosed ticket sizes: 85

Generating visualization data...
- Capital Flow Sankey
- Market Size Treemap
- Sectoral Investment Breakdown
- SDG Alignment
- Capital Source (Domestic vs International)
- Capital Instruments Timeline
- Top 10 Deals

All visualization data generated in 'data/' directory
```

### Step 3: View the Dashboard

**Option A: Using the launch script (recommended)**
```bash
python launch.py
```

**Option B: Using Python's built-in server**
```bash
python -m http.server 8000
```
Then open `http://localhost:8000/index.html` in your browser

**Option C: Direct file opening**
Simply double-click `index.html` (some features may be limited)

---

## 🎨 What You'll See

### Main Dashboard (`index.html`)

1. **Summary Statistics Cards**
   - Total Investment
   - Total Deals
   - Average Deal Size
   - Active Sectors

2. **Capital Flow Sankey**
   - Interactive flow diagram
   - Hover for details on each flow
   - Shows Investor Type → Sector relationships

3. **Market Size Treemap**
   - Click to drill down: Type → Institution → Sector
   - Color-coded by investment size
   - Hover for exact amounts

4. **Sectoral Investment Breakdown**
   - Toggle between Total Value and Deal Count
   - Stacked bars by year
   - See sector trends from 2021-2025

5. **SDG Alignment Wheel**
   - Donut chart showing SDG distribution
   - Identifies which SDGs attract most investment
   - Interactive legend

6. **Domestic vs International Capital**
   - Bar chart comparing Zambian vs foreign sources
   - See breakdown by investor type

7. **Capital Instruments Timeline**
   - Streamgraph showing evolution over time
   - Equity, Debt, Grant, Mezzanine, etc.
   - Hover for exact values per year

8. **Top 10 Deals Showcase**
   - Beautiful gradient cards
   - Shows largest disclosed investments
   - SDG tags and sector info

### Geographic Map (`map.html`)

- **Bubble map** of Zambian provinces
- **Regional bar chart** showing concentration
- Lusaka and Copperbelt dominate with 65% and 20% respectively

---

## 🎯 Key Features

### Interactive Elements

- **Hover** over any chart element for detailed information
- **Click** treemap sections to drill down
- **Toggle** between views (e.g., value vs. count)
- **Zoom** and pan on the geographic map

### Privacy Protection

- ✅ Anonymized firms excluded from individual displays
- ✅ Undisclosed amounts shown only in aggregates
- ✅ 10 anonymized deals filtered appropriately
- ✅ 85 deals with disclosed amounts displayed

### Mobile Responsive

- Works on desktop, tablet, and mobile
- Optimized layouts for all screen sizes
- Touch-friendly interactions

---

## 🔧 Troubleshooting

### Issue: "Module not found: pandas"
**Solution:** Install dependencies
```bash
pip install pandas openpyxl
```

### Issue: Charts not loading
**Solution:** Check that:
1. You ran `python process_data.py` first
2. The `data/` directory exists with 7 JSON files
3. You're using a local server (not opening file directly if issues persist)

### Issue: "Address already in use" (Port 8000 busy)
**Solution:** Use a different port
```bash
python -m http.server 8080
```
Then visit `http://localhost:8080`

### Issue: Browser shows blank page
**Solution:**
1. Open browser console (F12)
2. Check for errors
3. Ensure you're accessing via `http://localhost:8000`, not `file:///`

---

## 📊 Data Files Generated

After running `process_data.py`, you'll have:

```
data/
├── sankey_data.json           # Investor Type → Sector flows
├── treemap_data.json          # Hierarchical market composition
├── sectoral_data.json         # Sector trends by year
├── sdg_data.json              # SDG alignment totals
├── capital_source_data.json   # Domestic vs International
├── instrument_timeline.json   # Instruments over time
└── top_deals.json             # Top 10 disclosed deals
```

---

## 🎉 You're All Set!

Explore the interactive visualizations and discover insights about Zambia's Impact Investment Ecosystem!

### Next Steps

- Share the dashboard URL with your team
- Customize colors in `index.html` (search for `colorPalette`)
- Export charts using Plotly's built-in export button (📷 icon)
- Update data by modifying `Deal Data Zambia.xlsx` and re-running `process_data.py`

---

## 📞 Need Help?

Check the full documentation in `README.md` for:
- Detailed technical information
- Customization guides
- Data processing details
- Browser compatibility

---

**Happy Visualizing! 📈**
