# Interactive Chart Guide

A visual guide to understanding each chart in the NABII Impact Investment Dashboard.

---

## 1. Capital Flow Sankey Diagram

**What it shows:** How capital flows from investor types to sectors

**Reading the chart:**
- **Left side:** Investor types (DFI, VC, PE, Private Debt, Bank, Incubator, Pension Fund)
- **Right side:** Sectors (Energy, FinTech, Agriculture, etc.)
- **Flow width:** Proportional to investment amount in USD millions
- **Colors:** Different colors for each investor type and sector

**Hover to see:**
- Exact investment amount in USD millions
- Number of deals in that flow
- Source and target names

**Key insights:**
- Which investor types focus on which sectors
- Dominant capital flows (thickest bands)
- Sector attractiveness by total inflows

**Example:** "DFI → Energy & Renewable Power" shows how much DFI funding goes to energy sector

---

## 2. Market Size & Investor Composition Treemap

**What it shows:** Hierarchical breakdown of the market

**Structure:** 3 levels
1. **Investor Type** (outer boxes: DFI, VC, PE, etc.)
2. **Institution** (middle boxes: specific organizations)
3. **Sector** (inner boxes: where they invest)

**Reading the chart:**
- **Box size:** Proportional to total investment
- **Colors:** Different for each investor type
- **Labels:** Show name, amount, and percentage

**Interactivity:**
- **Click** any box to drill down
- **Hover** to see exact amounts
- Percentages shown relative to parent

**Key insights:**
- Market concentration (who controls most capital)
- Which institutions are most active
- Diversification of investor portfolios

**Example:** Large DFI box → Contains multiple institutions → Each investing in different sectors

---

## 3. Sectoral Investment Breakdown

**What it shows:** Investment trends by sector over time (2021-2025)

**Chart type:** Stacked bar chart

**Reading the chart:**
- **X-axis:** Years (2021, 2022, 2023, 2024, 2025)
- **Y-axis:** Total investment (USD millions) OR deal count
- **Colors:** Each color = different sector
- **Stack height:** Total investment per year

**Toggle buttons:**
- **Total Value (USD):** Shows dollar amounts
- **Deal Count:** Shows number of deals

**Key insights:**
- Which sectors are growing/declining
- Peak investment years
- Sector diversification over time
- COVID recovery patterns (2022 dip)

**Example:** 2024 shows tallest bar → highest investment year

---

## 4. SDG Alignment Wheel

**What it shows:** Total investment by Sustainable Development Goal

**Chart type:** Interactive donut (pie) chart

**Reading the chart:**
- **Segments:** Each slice = one SDG
- **Size:** Proportional to total investment in that SDG
- **Colors:** Official SDG colors (e.g., red for SDG 1, green for SDG 7)
- **Center text:** "SDG Impact"

**Hover to see:**
- SDG number and name
- Total investment amount
- Number of deals aligned to that SDG

**Key insights:**
- Which SDGs attract most capital
- Which SDGs are underserved
- Portfolio alignment with global goals

**Popular SDGs in Zambia:**
- SDG 7: Affordable and Clean Energy
- SDG 8: Decent Work and Economic Growth
- SDG 13: Climate Action

---

## 5. Domestic vs International Capital

**What it shows:** Comparison of Zambian vs. foreign investment sources

**Chart type:** Bar chart

**Reading the chart:**
- **X-axis:** Capital source (Domestic, International, Unknown)
- **Y-axis:** Total investment (USD millions)
- **Bar height:** Amount of capital
- **Labels:** Show exact USD amounts

**Hover to see:**
- Total investment value
- Number of deals
- Percentage of total

**Key insights:**
- Foreign vs. local capital ratio
- Self-sufficiency of domestic market
- DFI dominance (mostly international)

**Typical pattern:** International >> Domestic (due to DFI presence)

---

## 6. Capital Instruments Over Time

**What it shows:** Evolution of investment instruments (2021-2025)

**Chart type:** Streamgraph (stacked area chart)

**Reading the chart:**
- **X-axis:** Years
- **Y-axis:** Investment volume (USD millions)
- **Colored bands:** Different instruments (Equity, Debt, Grant, etc.)
- **Band width:** Amount invested via that instrument

**Instruments tracked:**
- **Equity:** Ownership stakes
- **Debt:** Loans and credit facilities
- **Grant:** Non-repayable funding
- **Mezzanine:** Hybrid debt-equity
- **Guarantee:** Credit guarantees
- **Convertible:** Convertible notes

**Key insights:**
- Instrument preferences over time
- Shift from grants to commercial capital
- Risk appetite evolution

**Example:** Wide equity band → equity is dominant instrument

---

## 7. Top 10 Deals Showcase

**What it shows:** Zambia's largest disclosed impact investments

**Format:** Interactive gradient cards (purple theme)

**Each card displays:**
- **Deal name** (e.g., "Africa Go Green Fund")
- **Ticket size** (large font, USD millions)
- **Investor** (who funded it)
- **Sector** (industry focus)
- **Year** (when it happened)
- **Investment type** (e.g., "PE - Equity")
- **SDG tags** (pills showing SDG numbers)

**Card ranking:**
- #1 = Largest deal
- #10 = 10th largest deal

**Interactivity:**
- **Hover** over card → slight zoom effect
- Cards display in priority order

**Privacy note:**
- Only shows deals with disclosed amounts
- Anonymized deals excluded
- 85 deals eligible, showing top 10

**Example Top Deal:**
```
#1 Africa Go Green Fund
$166.00M
Investor: Cygnum Capital
Sector: Climate & Clean Technology
Year: 2024
Type: PE - Equity
[SDG 7] [SDG 9] [SDG 13]
```

---

## 8. Geospatial Investment Map

**Location:** Separate page (map.html)

**What it shows:** Geographic distribution of investments across Zambia

### Map Visualization (Top)

**Chart type:** Bubble map overlaid on Zambia

**Reading the chart:**
- **Bubbles:** Each bubble = a province
- **Bubble size:** Proportional to investment concentration
- **Bubble color:** Heat map (yellow → pink → purple)
- **Labels:** Province names

**Hover to see:**
- Province name
- Total investment in that province (USD millions)

**Key provinces:**
- **Lusaka:** 65% of investment (capital city, largest bubble)
- **Copperbelt:** 20% of investment (mining region)
- **Others:** Smaller bubbles for remaining provinces

### Regional Bar Chart (Bottom)

**Chart type:** Horizontal bar chart

**Reading the chart:**
- **Y-axis:** Province names (sorted by investment)
- **X-axis:** Total investment (USD millions)
- **Bars:** Color-coded by amount
- **Labels:** Show percentage share

**Key insights:**
- Urban concentration of capital
- Infrastructure and business hub importance
- Regional inequality in investment

**Pattern:** Lusaka >> Copperbelt >> All others combined

---

## Interactive Features Across All Charts

### Hover Tooltips
Every chart element shows details on hover:
- Exact values (not just visual approximations)
- Multiple data points (e.g., USD + deal count)
- Clear labels

### Responsive Design
All charts automatically resize for:
- Desktop (full width)
- Tablet (medium width)
- Mobile (stacked layout)

### Plotly Controls
Each chart has built-in tools (top right):
- **Camera icon:** Download as PNG
- **Zoom icon:** Zoom in/out
- **Pan icon:** Move around
- **Home icon:** Reset view
- **Autoscale:** Fit to window

### Color Consistency
Colors are consistent across charts:
- Same investor type = same color
- Same sector = same color
- Professional gradient palette

---

## Reading Tips

### Understanding USD Millions
- $1.5M = $1,500,000 (one and a half million)
- $166M = $166,000,000 (one hundred sixty-six million)
- Total $1,509M = $1.509 billion

### Deal Counts vs. Values
- More deals ≠ more money (many small deals possible)
- Fewer deals with high values = concentrated capital
- Toggle between views to see both perspectives

### Anonymization
- Individual deals: Only non-anonymized shown
- Aggregate charts: All deals included
- No identification possible for protected firms

### Data Quality Indicators
- "Undisclosed" = amount not public
- Gray/minimal = low or unknown value
- Solid colors = confirmed data

---

## Chart Combinations for Insights

### Q: "Where is impact capital flowing?"
**Use:** Sankey + Sectoral Breakdown
**Insight:** See which sectors attract most investment over time

### Q: "Who are the major players?"
**Use:** Treemap + Top 10 Deals
**Insight:** Identify dominant institutions and their biggest deals

### Q: "Is the market growing?"
**Use:** Sectoral Breakdown + Instrument Timeline
**Insight:** See year-over-year trends and capital type evolution

### Q: "What's the SDG focus?"
**Use:** SDG Wheel + Top 10 Deals (check SDG tags)
**Insight:** Understand impact priorities and alignment

### Q: "Local vs. foreign capital?"
**Use:** Domestic vs International + Investor Composition
**Insight:** See capital sources and investor origin breakdown

### Q: "Where is money concentrated?"
**Use:** Geographic Map + Top 10 Deals
**Insight:** See both geographic and deal-level concentration

---

## Best Practices for Presentations

### For Investors
Focus on:
- Top 10 Deals (showcase opportunities)
- Sectoral Breakdown (identify gaps)
- SDG Alignment (impact thesis)

### For Policy Makers
Focus on:
- Domestic vs International (self-sufficiency)
- Geographic Map (regional inequality)
- Sectoral Breakdown (economic priorities)

### For Researchers
Focus on:
- All aggregate charts (comprehensive data)
- Instrument Timeline (market evolution)
- Capital Flow Sankey (network analysis)

### For General Audience
Focus on:
- Summary statistics (headline numbers)
- Top 10 Deals (success stories)
- Geographic Map (local relevance)

---

## Common Questions Answered

**Q: Why do some charts show different deal counts?**
A: Some deals lack certain fields (e.g., SDG tags). Each chart uses complete data for its specific purpose.

**Q: Why are values sometimes small or zero?**
A: Undisclosed amounts are shown as minimal values in aggregate charts for visualization purposes.

**Q: Can I export these charts?**
A: Yes! Use the camera icon (📷) in the top-right of each chart to download as PNG.

**Q: Why can't I see deal names in aggregate charts?**
A: Aggregate charts protect privacy by showing only totals, not individual deals.

**Q: How current is this data?**
A: Data spans 2021-2025 based on the Excel file. Update the file and reprocess to refresh.

---

## Navigation Tips

### Main Dashboard (index.html)
- Scroll down to see all 7 charts
- Click "View Interactive Map →" for geospatial view
- Summary statistics at the top

### Map Page (map.html)
- Click "← Back to Dashboard" to return
- Two visualizations: bubble map + bar chart
- Both show same data in different formats

### Mobile Viewing
- Charts stack vertically
- Toggle buttons remain functional
- Swipe to scroll through visualizations

---

**Ready to explore your data!** 📊

Each chart tells a part of Zambia's impact investment story. Together, they paint a comprehensive picture of the ecosystem from 2021-2025.
