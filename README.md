# Geospatial Data Analysis – Business Expansion Opportunities

A beginner-friendly Python project that explores location-based business data, maps sales and demand, and ranks areas that may offer expansion opportunities.

## Project objectives
- Visualize sales and demand by geographic location.
- Compare demand with the number of existing business locations.
- Calculate an illustrative unmet-demand score.
- Highlight candidate areas for further business research.

## Dataset
`data/geospatial_business_data.csv` contains **synthetic sample data** for selected areas in Nashik, Thane, and Pune, India. It is provided for learning and demonstration only; it is not actual market research or verified business data.

Important columns:
- `area`, `city`: location labels
- `latitude`, `longitude`: map coordinates
- `monthly_sales_units`: illustrative monthly sales
- `monthly_demand_index`: illustrative demand indicator
- `existing_business_locations`: sample count of existing businesses
- `estimated_unserved_demand`: simple proxy calculated as demand index minus 95 times existing locations, floored at zero

The score is a simplified educational proxy, not a statistically validated estimate of market demand.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run the analysis
```bash
python analysis.py
```
This creates CSV and PNG outputs in `outputs/`.

## Run the interactive map dashboard
```bash
streamlit run app.py
```
The dashboard includes city filters, KPI summaries, an interactive Folium map, and an opportunity ranking table.

## Tools used
Python, Pandas, Matplotlib, Folium, Streamlit.

## Suggested improvements
- Replace the sample CSV with verified sales and demographic data.
- Add population, rent, footfall, competitor distance, and operating cost.
- Validate the opportunity score with field research before making business decisions.
