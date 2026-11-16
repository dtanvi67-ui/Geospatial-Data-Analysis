from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "geospatial_business_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df["demand_per_existing_location"] = (
    df["monthly_demand_index"] / df["existing_business_locations"].clip(lower=1)
)
df["opportunity_score"] = (
    0.6 * df["estimated_unserved_demand"] +
    0.4 * df["demand_per_existing_location"]
).round(2)

city_summary = df.groupby("city", as_index=False).agg(
    total_sales_units=("monthly_sales_units", "sum"),
    average_demand_index=("monthly_demand_index", "mean"),
    existing_locations=("existing_business_locations", "sum"),
    opportunity_score=("opportunity_score", "mean"),
)
city_summary.to_csv(OUT / "city_summary.csv", index=False)

ranking = df.sort_values("opportunity_score", ascending=False)
ranking.to_csv(OUT / "area_opportunity_ranking.csv", index=False)

plt.figure(figsize=(10, 6))
top = ranking.head(10).sort_values("opportunity_score")
plt.barh(top["area"] + ", " + top["city"], top["opportunity_score"])
plt.xlabel("Illustrative opportunity score")
plt.title("Top 10 Areas by Opportunity Score")
plt.tight_layout()
plt.savefig(OUT / "top_opportunity_areas.png", dpi=160)
plt.close()

plt.figure(figsize=(9, 6))
plt.scatter(df["longitude"], df["latitude"], s=df["monthly_sales_units"] / 3,
            c=df["estimated_unserved_demand"], alpha=0.75)
for _, row in df.iterrows():
    plt.annotate(row["area"], (row["longitude"], row["latitude"]), fontsize=7)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Sample Sales Locations (bubble size = sales; color = unmet-demand proxy)")
plt.tight_layout()
plt.savefig(OUT / "location_scatter.png", dpi=160)
plt.close()

print("Analysis complete.")
print(f"Areas analysed: {len(df)}")
print(f"Total sample sales units: {df['monthly_sales_units'].sum():,}")
print("Top 5 candidate areas:")
print(ranking[["area", "city", "opportunity_score"]].head(5).to_string(index=False))
print(f"Outputs saved in: {OUT}")
