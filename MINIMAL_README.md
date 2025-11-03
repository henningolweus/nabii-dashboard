# Minimal NABII Dashboard

A streamlined version of the Zambia Impact Investment Dashboard featuring only the two most essential visualizations.

## 📊 What's Included

### 1. **Summary Statistics**
- Total Investment
- Total Deals
- Average Deal Size
- Active Sectors

### 2. **Capital Flow Network (Sankey Diagram)**
- Visual representation of capital movement
- Investor types → Sectors
- Interactive hover to see investment amounts and deal counts

### 3. **Sectoral Investment Trends**
- Stacked bar chart showing investment evolution
- Toggle between Total Value (USD) and Deal Count
- Year-by-year breakdown by sector
- Interactive legend

## 🎨 Design

- Clean, minimal interface
- Full NABII branding (green #1A6B18, navy #121C27, beige #ECE6E1)
- Roboto & Public Sans fonts
- Fully responsive (mobile-optimized)
- No decimals on axes
- Professional presentation-ready design

## 📦 Data Requirements

Only 2 JSON files needed:
- `data/sankey_data.json` - Capital flow data
- `data/sectoral_data.json` - Sectoral investment by year

## 🚀 How to Use

### View Locally
```bash
# Open index.html in your browser
# or use Python's built-in server:
python -m http.server 8000
# Visit: http://localhost:8000
```

### Deploy on GitHub Pages

#### **Option 1: Publish Minimal Branch**
1. Go to your repository: https://github.com/henningolweus/nabii-dashboard
2. Click **Settings** → **Pages**
3. Under "Source", select **minimal** branch (instead of main)
4. Click **Save**
5. Your minimal dashboard will be live at: `https://henningolweus.github.io/nabii-dashboard/`

#### **Option 2: Create Separate Repository**
```bash
# Create new repo on GitHub: nabii-dashboard-minimal
cd "C:\Users\heol\Documents\Coding\Projects\NABII Interactive Charts"
git remote add minimal-origin https://github.com/henningolweus/nabii-dashboard-minimal.git
git push minimal-origin minimal:main
```
Then enable GitHub Pages for the new repository.

## 🔄 Switching Versions

### Switch to Minimal Branch
```bash
git checkout minimal
```

### Switch Back to Full Dashboard
```bash
git checkout main
```

## 📝 Differences from Full Version

**Removed:**
- ❌ SDG Impact Alignment chart
- ❌ Capital Sources chart
- ❌ Investment Instruments timeline
- ❌ Investor Type Distribution
- ❌ Top Performing Sectors
- ❌ Top 10 Deals showcase
- ❌ World heat map page

**Kept:**
- ✅ Summary statistics (4 cards)
- ✅ Sankey diagram (capital flow)
- ✅ Sectoral investment trends

## 💡 Use Cases

Perfect for:
- Executive presentations
- Quick insights and overviews
- Embedded dashboards
- Email reports
- Mobile viewing
- Low-bandwidth environments
- Focus on key metrics only

## 📊 File Size Comparison

- **Full Dashboard**: ~1,220 lines (index.html)
- **Minimal Dashboard**: ~632 lines (index.html)
- **Reduction**: ~48% smaller

## 🌐 Live URLs

- **Full Dashboard**: https://henningolweus.github.io/nabii-dashboard/ (main branch)
- **Minimal Dashboard**: Configure in Settings → Pages → select "minimal" branch

## 🛠️ Technical Details

**Libraries:**
- ApexCharts 3.45.1 (sectoral chart)
- Plotly.js 2.27.0 (Sankey diagram)
- Google Fonts (Roboto, Public Sans)

**Browser Support:**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📱 Responsive Breakpoints

- **Desktop**: 1500px max-width
- **Tablet**: 1024px
- **Mobile**: 767px

## 🎯 Quick Stats

- **Load Time**: < 2 seconds
- **Charts**: 2 interactive visualizations
- **Data Files**: 2 JSON files
- **Total Size**: ~50KB (with data)

---

**Built for NABII · Zambia Impact Investment Ecosystem**
