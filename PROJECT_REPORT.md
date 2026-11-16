# Project Report: Geospatial Data Analysis

## 1. Introduction
Geospatial analysis uses location information to understand patterns across geographic areas. Businesses can use maps alongside sales and demand indicators to explore where expansion may be worth investigating.

## 2. Problem statement
A business needs to compare sales, demand, and current business presence across multiple areas to identify candidate locations for further study.

## 3. Objectives
1. Organize location-based data with latitude and longitude.
2. Visualize sample sales locations on an interactive map.
3. Compare demand indicators with existing business presence.
4. Rank areas using a transparent, illustrative opportunity score.

## 4. Methodology
The project loads a CSV dataset with Pandas, calculates an unmet-demand proxy, and combines it with demand per existing location. The resulting opportunity score is used only to sort sample areas. Folium displays the locations on a map, while Streamlit provides filters and summary metrics.

## 5. Opportunity score
`opportunity_score = 0.6 × estimated_unserved_demand + 0.4 × demand_per_existing_location`

`estimated_unserved_demand = max(0, monthly_demand_index − 95 × existing_business_locations)`

These formulas are deliberately simple teaching examples. Their weights and assumptions are not validated and should be replaced with business-specific measures.

## 6. Expected outcomes
- A geographic view of sample sales locations.
- A comparison of demand indicators and existing presence.
- A ranked list of areas to investigate.
- Reproducible analysis outputs and an interactive dashboard.

## 7. Limitations
The included data is synthetic. It does not establish actual demand, competitor coverage, population, rent, profitability, or expansion suitability. A real study would require reliable data, geographic validation, and field research.

## 8. Conclusion
The project demonstrates how Python mapping and data analysis can support location-based exploration. It provides a starting workflow that can be extended with verified business and demographic data.
