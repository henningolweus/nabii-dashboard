# Zambia Impact Investment Ecosystem - Interactive Dashboard

A sleek, interactive web visualization dashboard showcasing Zambia's Impact Investment Ecosystem for NABII (National Angel & Business Impact Initiative).

## Overview

This project visualizes key insights from Zambia's impact investment landscape (2021-2025), including:
- Capital flows between investor types and sectors
- Market composition and concentration
- Sectoral trends over time
- SDG alignment of investments
- Domestic vs. international capital sources
- Evolution of investment instruments
- Top impactful deals
- Geographic distribution of investments

## Features

### 8 Interactive Visualizations

1. **Capital Flow Sankey Diagram** - Shows how capital moves from investor types (DFI, VC, PE, etc.) to sectors
2. **Market Size Treemap** - Hierarchical view of Investor Type → Institution → Sector
3. **Sectoral Investment Breakdown** - Stacked bar chart showing investment trends by sector over years
4. **SDG Alignment Wheel** - Donut chart displaying investment by Sustainable Development Goal
5. **Domestic vs International Capital** - Comparison of Zambian vs. foreign investment sources
6. **Capital Instruments Timeline** - Streamgraph showing evolution of Equity, Debt, Grant, etc.
7. **Top 10 Deals Showcase** - Interactive cards highlighting the most impactful investments
8. **Geospatial Investment Map** - Geographic distribution across Zambian provinces

### Privacy Features

- **Anonymized firms are excluded** from individual deal displays
- **Undisclosed deal sizes** appear only in aggregated views
- 10 anonymized deals filtered from individual showcase
- 85 deals with disclosed amounts shown in detail

## Project Structure

```
NABII Interactive Charts/
│
├── Deal Data Zambia.xlsx        # Source data file
├── process_data.py              # Python data processing pipeline
├── index.html                   # Main dashboard
├── map.html                     # Geospatial map page
├── README.md                    # This file
│
└── data/                        # Generated JSON data files
    ├── sankey_data.json
    ├── treemap_data.json
    ├── sectoral_data.json
    ├── sdg_data.json
    ├── capital_source_data.json
    ├── instrument_timeline.json
    └── top_deals.json
```

## Installation & Setup

### Prerequisites

- Python 3.7+
- pandas library
- openpyxl library (for Excel file reading)

### Step 1: Install Python Dependencies

```bash
pip install pandas openpyxl
```

### Step 2: Process the Data

Run the data processing script to generate JSON files:

```bash
python process_data.py
```

This will:
- Read the Excel file
- Filter anonymized/undisclosed data appropriately
- Generate 7 JSON files in the `data/` directory
- Display processing statistics

### Step 3: View the Dashboard

Open `index.html` in a modern web browser:

```bash
# Using Python's built-in server (recommended)
python -m http.server 8000

# Then open: http://localhost:8000
```

Or simply double-click `index.html` to open directly in your browser.

### Step 4: Explore the Map

Click "View Interactive Map →" on the main dashboard, or open `map.html` directly.

## Data Processing Details

### Ticket Size Parsing

The pipeline automatically:
- Extracts numeric values from various formats ("USD 3 million", "USD 0.5 million", etc.)
- Converts to millions for consistency
- Flags "Undisclosed" and "Not disclosed" entries as `null`

### Anonymization Logic

```python
# Individual display filtering
df['Show_Individual'] = ~df['Anonymized'] & df['Ticket_Size_USD_Millions'].notna()
```

- Deals marked `Anonymized=True` → excluded from Top 10 and individual cards
- Undisclosed ticket sizes → excluded from individual displays
- **All data included** in aggregate charts (Sankey, treemap, etc.)

### SDG Extraction

Parses SDG references from text:
```
"SDG 7 (Affordable and Clean Energy), SDG 13 (Climate Action)"
→ [7, 13]
```

### Capital Source Classification

- `Country of Origin = "Zambia"` → Domestic
- All other countries → International

## Key Statistics

Based on processed data:

| Metric | Value |
|--------|-------|
| **Total Records** | 128 deals |
| **Deals with Disclosed Amounts** | 85 deals |
| **Anonymized Deals** | 10 deals |
| **Years Covered** | 2021-2025 |
| **Investor Types** | DFI, VC, PE, Private Debt, Bank, Incubator, Pension Fund |
| **Sectors** | 8 mapped sectors |
| **Instruments** | Equity, Debt, Grant, Mezzanine, Guarantee, Convertible |

## Technology Stack

### Frontend
- **ApexCharts 3.45.1** - Modern, professional charting library
- **Pure JavaScript** - No frameworks, lightweight and fast
- **CSS3** - NABII brand colors and clean design
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Google Fonts** - Roboto & Public Sans typography

### Backend
- **Python 3** - Data processing
- **pandas** - Data manipulation and analysis
- **JSON** - Data interchange format

## Browser Support

Tested and working on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Customization

### Changing Colors

Edit the color palettes in `index.html`:

```javascript
const colorPalette = ['#667eea', '#764ba2', '#f093fb', '#4facfe', ...];
```

### Adding More Visualizations

1. Add data processing function in `process_data.py`
2. Export JSON file
3. Add chart container in `index.html`
4. Implement rendering function with Plotly

### Modifying Filters

Edit the filtering logic in `process_data.py`:

```python
def generate_top_deals(df, n=10):
    # Modify filtering criteria here
    top_deals_df = df[df['Show_Individual']].copy()
```

## Data Privacy & Ethics

This dashboard adheres to data privacy principles:

✅ **Anonymized firms** protected from individual identification
✅ **Undisclosed amounts** kept confidential
✅ **Aggregate insights** maintain statistical value
✅ **Transparent methodology** documented in code

## Future Enhancements

Potential additions:
- [ ] Filter by year range dynamically
- [ ] Export charts as PNG/PDF
- [ ] Drill-down capability in treemap
- [ ] Real-time data updates from API
- [ ] Comparison mode (year-over-year)
- [ ] Search functionality for deals
- [ ] Enhanced geographic mapping with Mapbox

## Credits

**Data Visualization:** NABII (National Angel & Business Impact Initiative)
**Data Source:** Deal Data Zambia.xlsx
**Technology:** ApexCharts, Python, pandas
**Design:** Professional NABII-branded design with green accent colors

## License

This visualization dashboard is created for NABII. Please contact NABII for usage permissions.

## Contact & Support

For questions about the data or visualizations:
- **Organization:** NABII (National Angel & Business Impact Initiative)
- **Website:** [Add NABII website]
- **Email:** [Add contact email]

---

**Built with ❤️ for Zambia's Impact Investment Ecosystem**
