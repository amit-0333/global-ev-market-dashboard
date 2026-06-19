import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# page config
st.set_page_config(page_title="Global EV Market Dashboard", layout="wide")

sns.set_style("whitegrid")

# load data
@st.cache_data
def load_data():
    df = pd.read_csv("global_ev_market_cleaned.csv")
    return df

df = load_data()

st.title("Global Electric Vehicle Market Dashboard (2026)")
st.caption("Country-wise EV sales, battery specs, and charging infrastructure")

# sidebar filters
st.sidebar.header("Filters")

# region single select, default Asia, drives the whole page
regions = sorted(df["region"].unique())
default_region_index = regions.index("Asia") if "Asia" in regions else 0
selected_region = st.sidebar.selectbox("Region", regions, index=default_region_index)

# country cascades from selected region, drives the whole page
countries_in_region = sorted(df[df["region"] == selected_region]["country"].unique())
selected_country = st.sidebar.selectbox("Country", countries_in_region)

# govt incentives is an active filter
incentive_option = st.sidebar.selectbox("Govt Incentives", ["All", "Yes", "No"])

# apply active filters: region, country, and govt incentives only
filtered_df = df[
    (df["region"] == selected_region)
    & (df["country"] == selected_country)
]

if incentive_option != "All":
    filtered_df = filtered_df[filtered_df["govt_incentives"] == incentive_option]

# handle empty result
if filtered_df.empty:
    st.warning("No data matches the selected filters. Please adjust your selection.")
    st.stop()

st.subheader(f"Showing data for {selected_country} ({selected_region})")

# KPI summary
st.subheader("Summary")
col1, col2, col3, col4 = st.columns(4)

total_sales = filtered_df["ev_sales_units"].sum()
num_vehicle_types = filtered_df["vehicle_type"].nunique()
top_brand = filtered_df.groupby("ev_brand")["ev_sales_units"].sum().idxmax()
avg_range = filtered_df["vehicle_range_km"].mean()
avg_capacity = filtered_df["battery_capacity_kwh"].mean()

col1.metric("Total EV Units Sold", f"{total_sales:,.0f}")
col2.metric("Vehicle Types Covered", num_vehicle_types)
col3.metric("Top-Selling Brand", top_brand)
col4.metric("Avg Battery Capacity / Range", f"{avg_capacity:.0f} kWh / {avg_range:.0f} km")

st.divider()

# chart 1: sales by vehicle type for the selected country
st.subheader(f"EV Sales by Vehicle Type in {selected_country}")
sales_by_vehicle_type = (
    filtered_df.groupby("vehicle_type")["ev_sales_units"]
    .sum()
    .sort_values(ascending=False)
)
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.barplot(x=sales_by_vehicle_type.index, y=sales_by_vehicle_type.values, hue=sales_by_vehicle_type.index, palette="Blues_d", legend=False, ax=ax1)
ax1.set_xlabel("Vehicle Type")
ax1.set_ylabel("EV Units Sold")
ax1.set_title(f"Total EV Sales by Vehicle Type in {selected_country}")
st.pyplot(fig1)

# chart 2: sales by region, shown for broader context against the selected country's region
st.subheader("EV Sales by Region")
st.caption("The dataset only covers a single year (2026), so this view replaces a year-over-year trend chart.")
sales_by_region = df.groupby("region")["ev_sales_units"].sum().sort_values(ascending=False)
fig2, ax2 = plt.subplots(figsize=(8, 5))
bar_colors = ["#c0392b" if region == selected_region else "#3b82c4" for region in sales_by_region.index]
sns.barplot(x=sales_by_region.index, y=sales_by_region.values, hue=sales_by_region.index, palette=bar_colors, legend=False, ax=ax2)
ax2.set_xlabel("Region")
ax2.set_ylabel("EV Units Sold")
ax2.set_title(f"Total EV Sales by Region (Highlighted: {selected_region})")
st.pyplot(fig2)

col5, col6 = st.columns(2)

with col5:
    st.subheader(f"Market Share by Vehicle Type in {selected_country}")
    market_share = filtered_df.groupby("vehicle_type")["ev_sales_units"].sum()
    fig3, ax3 = plt.subplots(figsize=(6, 6))
    ax3.pie(market_share.values, labels=market_share.index, autopct="%1.1f%%", startangle=90)
    ax3.set_title(f"Market Share by Vehicle Type in {selected_country}")
    st.pyplot(fig3)

with col6:
    st.subheader(f"Top Manufacturers by Sales in {selected_country}")
    top_brands = filtered_df.groupby("ev_brand")["ev_sales_units"].sum().sort_values(ascending=False)
    fig4, ax4 = plt.subplots(figsize=(6, 6))
    sns.barplot(x=top_brands.values, y=top_brands.index, hue=top_brands.index, palette="Greens_d", legend=False, ax=ax4)
    ax4.set_xlabel("EV Units Sold")
    ax4.set_ylabel("Manufacturer")
    ax4.set_title(f"Total EV Sales by Manufacturer in {selected_country}")
    st.pyplot(fig4)

st.subheader(f"Battery Capacity vs Vehicle Range in {selected_country}")
fig5, ax5 = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=filtered_df, x="battery_capacity_kwh", y="vehicle_range_km", hue="vehicle_type", alpha=0.6, ax=ax5)
ax5.set_xlabel("Battery Capacity (kWh)")
ax5.set_ylabel("Vehicle Range (km)")
ax5.set_title(f"Battery Capacity vs Vehicle Range in {selected_country}")
st.pyplot(fig5)

st.divider()

# data table for current selection
st.subheader("Filtered Data")
st.dataframe(filtered_df, use_container_width=True)

# download button
csv_data = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name=f"{selected_country}_ev_data.csv",
    mime="text/csv",
)