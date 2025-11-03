"""
NABII Impact Investment Data Processing Pipeline
Processes Zambia's Impact Investment Ecosystem data for interactive visualizations
"""

import pandas as pd
import numpy as np
import json
import re
from datetime import datetime

def parse_ticket_size(ticket_str):
    """Convert ticket size strings to numeric USD values in millions"""
    if pd.isna(ticket_str) or ticket_str in ['Undisclosed', 'Not disclosed', 'undisclosed', 'not disclosed']:
        return None

    # Extract numeric value
    match = re.search(r'[\d.]+', str(ticket_str))
    if match:
        value = float(match.group())
        # Handle different units (assuming millions if 'million' in string)
        if 'million' in str(ticket_str).lower():
            return value
        return value
    return None

def extract_sdgs(sdg_str):
    """Extract SDG numbers from SDG string"""
    if pd.isna(sdg_str):
        return []

    # Find all SDG numbers (e.g., "SDG 7", "SDG 13")
    sdgs = re.findall(r'SDG\s*(\d+)', str(sdg_str))
    return [int(sdg) for sdg in sdgs]

def classify_domestic_international(country):
    """Classify investor as domestic (Zambian) or international"""
    if pd.isna(country):
        return 'Unknown'
    return 'Domestic' if country == 'Zambia' else 'International'

def load_and_process_data(filepath):
    """Load Excel data and process for visualizations"""

    print("Loading data from Excel...")
    df = pd.read_excel(filepath)

    print(f"Total records: {len(df)}")

    # Map unmapped sectors to appropriate categories
    sector_mapping = {
        'Biopharmaceuticals': 'Healthcare & Education',
        'Pharmaceuticals': 'Healthcare & Education',
        'Telecommunications': 'Technology & Digital Services',
        'Tourism': 'Manufacturing & Other'
    }

    # Fill missing Mapped_Sector using Deal1_Sector
    for idx, row in df.iterrows():
        if pd.isna(row['Mapped_Sector']) and pd.notna(row['Deal1_Sector']):
            sector = row['Deal1_Sector']
            df.at[idx, 'Mapped_Sector'] = sector_mapping.get(sector, 'Manufacturing & Other')

    # Use Deal1_Ticket USD column directly (already in millions)
    df['Ticket_Size_USD_Millions'] = df['Deal1_Ticket USD']

    # For anonymized/undisclosed deals, the Deal1_Ticket USD might have placeholder values
    # We need to mark those as should not be shown individually
    df['Has_Disclosed_Amount'] = df['Deal1_Ticket'].apply(
        lambda x: False if pd.isna(x) or str(x).lower() in ['undisclosed', 'not disclosed'] else True
    )

    # Extract SDG numbers
    df['SDG_List'] = df['Deal1_SDG'].apply(extract_sdgs)

    # Classify domestic vs international
    df['Capital_Source'] = df['Country of Origin'].apply(classify_domestic_international)

    # Filter out anonymized deals AND undisclosed amounts for individual display
    df['Show_Individual'] = ~df['Anonymized'] & df['Has_Disclosed_Amount']

    print(f"Anonymized deals (excluded from individual display): {df['Anonymized'].sum()}")
    print(f"Deals with disclosed ticket sizes: {df['Has_Disclosed_Amount'].sum()}")
    print(f"Deals eligible for individual display: {df['Show_Individual'].sum()}")

    return df

def generate_sankey_data(df):
    """Generate Sankey diagram data: Investor Type -> Sector"""

    # Use ALL data - Deal1_Ticket USD has values for all records
    sankey_df = df.copy()

    # Sum ticket sizes and count deals
    flows = sankey_df.groupby(['Segment', 'Mapped_Sector']).agg({
        'Ticket_Size_USD_Millions': 'sum',
        'Deal1_Name': 'count'
    }).reset_index()

    flows.columns = ['source', 'target', 'value', 'deal_count']

    # Create node lists
    sources = flows['source'].unique().tolist()
    targets = flows['target'].unique().tolist()
    all_nodes = sources + [t for t in targets if t not in sources]

    # Map to indices
    node_dict = {node: idx for idx, node in enumerate(all_nodes)}

    sankey_data = {
        'nodes': [{'name': node} for node in all_nodes],
        'links': [
            {
                'source': node_dict[row['source']],
                'target': node_dict[row['target']],
                'value': float(row['value']),
                'deal_count': int(row['deal_count'])
            }
            for _, row in flows.iterrows()
        ]
    }

    return sankey_data

def generate_treemap_data(df):
    """Generate treemap data: Investor Type -> Institution -> Sector"""

    # Use all data with actual ticket values
    treemap_df = df.copy()

    children = []

    for segment in treemap_df['Segment'].unique():
        segment_data = treemap_df[treemap_df['Segment'] == segment]

        investor_children = []
        for investor in segment_data['Investor'].unique():
            investor_data = segment_data[segment_data['Investor'] == investor]

            sector_children = []
            for sector in investor_data['Mapped_Sector'].unique():
                sector_data = investor_data[investor_data['Mapped_Sector'] == sector]
                total_value = sector_data['Ticket_Size_USD_Millions'].sum()

                sector_children.append({
                    'name': sector,
                    'value': float(total_value),
                    'deal_count': len(sector_data)
                })

            investor_children.append({
                'name': investor,
                'children': sector_children
            })

        children.append({
            'name': segment,
            'children': investor_children
        })

    treemap_data = {
        'name': 'Zambia Impact Investment',
        'children': children
    }

    return treemap_data

def generate_sectoral_breakdown(df):
    """Generate sectoral investment breakdown by year"""

    # Use all data with actual ticket values
    sectoral_df = df.copy()

    # Group by year and sector
    breakdown = sectoral_df.groupby(['Deal1_Year', 'Mapped_Sector']).agg({
        'Ticket_Size_USD_Millions': 'sum',
        'Deal1_Name': 'count'
    }).reset_index()

    breakdown.columns = ['year', 'sector', 'total_value', 'deal_count']

    # Convert to format for stacked chart
    data_by_year = {}
    for year in sorted(breakdown['year'].unique()):
        year_data = breakdown[breakdown['year'] == year]
        data_by_year[int(year)] = {
            'sectors': year_data['sector'].tolist(),
            'values': year_data['total_value'].tolist(),
            'counts': year_data['deal_count'].tolist()
        }

    return data_by_year

def generate_sdg_data(df):
    """Generate SDG alignment data"""

    # Use all data with actual ticket values
    sdg_df = df.copy()

    # Expand SDG lists
    sdg_records = []
    for _, row in sdg_df.iterrows():
        for sdg in row['SDG_List']:
            sdg_records.append({
                'sdg': sdg,
                'value': row['Ticket_Size_USD_Millions'],
                'deal_name': row['Deal1_Name']
            })

    sdg_summary = pd.DataFrame(sdg_records)

    if len(sdg_summary) > 0:
        sdg_totals = sdg_summary.groupby('sdg').agg({
            'value': 'sum',
            'deal_name': 'count'
        }).reset_index()

        sdg_totals.columns = ['sdg', 'total_investment', 'deal_count']

        # SDG names mapping
        sdg_names = {
            1: 'No Poverty', 2: 'Zero Hunger', 3: 'Good Health',
            4: 'Quality Education', 5: 'Gender Equality', 6: 'Clean Water',
            7: 'Clean Energy', 8: 'Decent Work', 9: 'Innovation',
            10: 'Reduced Inequalities', 11: 'Sustainable Cities', 12: 'Responsible Consumption',
            13: 'Climate Action', 14: 'Life Below Water', 15: 'Life on Land',
            16: 'Peace & Justice', 17: 'Partnerships'
        }

        sdg_totals['name'] = sdg_totals['sdg'].apply(lambda x: f"SDG {x}: {sdg_names.get(x, 'Unknown')}")

        return sdg_totals.to_dict('records')

    return []

def generate_capital_source_data(df):
    """Generate domestic vs international capital comparison"""

    # Use all data with actual ticket values
    capital_df = df.copy()

    source_summary = capital_df.groupby('Capital_Source').agg({
        'Ticket_Size_USD_Millions': 'sum',
        'Deal1_Name': 'count'
    }).reset_index()

    source_summary.columns = ['source', 'total_value', 'deal_count']

    # Add investor type breakdown
    detailed = capital_df.groupby(['Capital_Source', 'Segment']).agg({
        'Ticket_Size_USD_Millions': 'sum'
    }).reset_index()

    return {
        'summary': source_summary.to_dict('records'),
        'by_type': detailed.to_dict('records')
    }

def generate_instrument_timeline(df):
    """Generate capital instruments over time data"""

    # Use all data with actual ticket values
    instrument_df = df.copy()

    timeline = instrument_df.groupby(['Deal1_Year', 'Instrument_Type']).agg({
        'Ticket_Size_USD_Millions': 'sum',
        'Deal1_Name': 'count'
    }).reset_index()

    timeline.columns = ['year', 'instrument', 'value', 'count']

    return timeline.to_dict('records')

def generate_top_deals(df, n=10):
    """Generate top N deals showcase"""

    # Only show non-anonymized deals with disclosed sizes
    top_deals_df = df[df['Show_Individual']].copy()

    # Sort by ticket size
    top_deals_df = top_deals_df.nlargest(n, 'Ticket_Size_USD_Millions')

    deals = []
    for _, row in top_deals_df.iterrows():
        deals.append({
            'name': row['Deal1_Name'],
            'investor': row['Investor'],
            'sector': row['Mapped_Sector'],
            'year': int(row['Deal1_Year']),
            'ticket_size': float(row['Ticket_Size_USD_Millions']),
            'instrument': row['Instrument_Type'],
            'sdgs': row['SDG_List'],
            'details': row.get('Deal1_Investment Details', ''),
            'segment': row['Segment']
        })

    return deals

def generate_country_data(df):
    """Generate geographic data by country of capital origin"""

    # Use all data with actual ticket values
    country_df = df[df['Country of Origin'].notna()].copy()

    # Group by country
    country_summary = country_df.groupby('Country of Origin').agg({
        'Ticket_Size_USD_Millions': 'sum',
        'Deal1_Name': 'count'
    }).reset_index()

    country_summary.columns = ['country', 'total_investment', 'deal_count']

    # Sort by investment amount
    country_summary = country_summary.sort_values('total_investment', ascending=False)

    return country_summary.to_dict('records')

def generate_all_visualizations(filepath, output_dir='data'):
    """Generate all visualization data files"""

    import os
    os.makedirs(output_dir, exist_ok=True)

    # Load and process data
    df = load_and_process_data(filepath)

    print("\nGenerating visualization data...")

    # 1. Sankey
    print("- Capital Flow Sankey")
    sankey_data = generate_sankey_data(df)
    with open(f'{output_dir}/sankey_data.json', 'w') as f:
        json.dump(sankey_data, f, indent=2)

    # 2. Treemap
    print("- Market Size Treemap")
    treemap_data = generate_treemap_data(df)
    with open(f'{output_dir}/treemap_data.json', 'w') as f:
        json.dump(treemap_data, f, indent=2)

    # 3. Sectoral breakdown
    print("- Sectoral Investment Breakdown")
    sectoral_data = generate_sectoral_breakdown(df)
    with open(f'{output_dir}/sectoral_data.json', 'w') as f:
        json.dump(sectoral_data, f, indent=2)

    # 4. SDG alignment
    print("- SDG Alignment")
    sdg_data = generate_sdg_data(df)
    with open(f'{output_dir}/sdg_data.json', 'w') as f:
        json.dump(sdg_data, f, indent=2)

    # 5. Capital source
    print("- Capital Source (Domestic vs International)")
    capital_data = generate_capital_source_data(df)
    with open(f'{output_dir}/capital_source_data.json', 'w') as f:
        json.dump(capital_data, f, indent=2)

    # 6. Instrument timeline
    print("- Capital Instruments Timeline")
    instrument_data = generate_instrument_timeline(df)
    with open(f'{output_dir}/instrument_timeline.json', 'w') as f:
        json.dump(instrument_data, f, indent=2)

    # 7. Top deals
    print("- Top 10 Deals")
    top_deals = generate_top_deals(df, n=10)
    with open(f'{output_dir}/top_deals.json', 'w') as f:
        json.dump(top_deals, f, indent=2)

    # 8. Country geographic data
    print("- Country Geographic Data")
    country_data = generate_country_data(df)
    with open(f'{output_dir}/country_data.json', 'w') as f:
        json.dump(country_data, f, indent=2)

    print(f"\nAll visualization data generated in '{output_dir}/' directory")
    print("Ready to create interactive visualizations!")

    return df

if __name__ == '__main__':
    df = generate_all_visualizations('Deal Data Zambia.xlsx')
