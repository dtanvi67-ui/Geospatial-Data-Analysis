from pathlib import Path
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "data" / "geospatial_business_data.csv")
df["demand_per_existing_location"] = (
    df["monthly_demand_index"] / df["existing_business_locations"].clip(lower=1)
)
df["opportunity_score"] = (
    0.6 * df["estimated_unserved_demand"] +
    0.4 * df["demand_per_existing_location"]
).round(2)

st.set_page_config(page_title="Geospatial Business Analysis", layout="wide")
st.title("Geospatial Data Analysis")
st.caption("Explore illustrative sales, demand, and potential expansion areas.")

cities = ["All"] + sorted(df["city"].unique().tolist())
selected_city = st.sidebar.selectbox("Select city", cities)
view = df if selected_city == "All" else df[df["city"] == selected_city]

c1, c2, c3 = st.columns(3)
c1.metric("Areas analysed", len(view))
c2.metric("Total sample sales", f"{view['monthly_sales_units'].sum():,} units")
c3.metric("Average demand index", f"{view['monthly_demand_index'].mean():.0f}")

st.subheader("Location map")
center = [view["latitude"].mean(), view["longitude"].mean()]
m = folium.Map(location=center, zoom_start=10, tiles="CartoDB positron")
max_score = max(float(view["opportunity_score"].max()), 1)
for _, r in view.iterrows():
    radius = 5 + 10 * float(r["opportunity_score"]) / max_score
    popup = (
        f"<b>{r['area']}, {r['city']}</b><br>"
        f"Sales units: {r['monthly_sales_units']}<br>"
        f"Demand index: {r['monthly_demand_index']}<br>"
        f"Existing locations: {r['existing_business_locations']}<br>"
        f"Opportunity score: {r['opportunity_score']}"
    )
    folium.CircleMarker(
        location=[r["latitude"], r["longitude"]],
        radius=radius, popup=popup, tooltip=f"{r['area']} – {r['city']}",
        color="#2457A7", fill=True, fill_opacity=0.65
    ).add_to(m)
st_folium(m, width=None, height=520)

st.subheader("Areas ranked by illustrative opportunity score")
ranked = view.sort_values("opportunity_score", ascending=False)
st.dataframe(
    ranked[["area", "city", "monthly_sales_units", "monthly_demand_index",
            "existing_business_locations", "estimated_unserved_demand",
            "opportunity_score"]].reset_index(drop=True),
    use_container_width=True
)

st.subheader("Sales by area")
chart = view.set_index("area")[["monthly_sales_units"]].sort_values("monthly_sales_units")
st.bar_chart(chart)

st.info(
    "This dashboard uses synthetic demonstration data. The opportunity score is a "
    "simple proxy for learning, not a validated market forecast. Verify real demand, "
    "competition, costs, and local conditions before making business decisions."
)
