<div align="center">

```
███████╗██╗   ██╗    ███╗   ███╗ █████╗ ██████╗ ██╗  ██╗███████╗████████╗
██╔════╝██║   ██║    ████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██╔════╝╚══██╔══╝
█████╗  ██║   ██║    ██╔████╔██║███████║██████╔╝█████╔╝ █████╗     ██║   
██╔══╝  ╚██╗ ██╔╝    ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝     ██║   
███████╗ ╚████╔╝     ██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗███████╗   ██║   
╚══════╝  ╚═══╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   
```

### 🌍 Global Electric Vehicle Market Dashboard (2026)

> An interactive Streamlit dashboard exploring country-wise EV sales, battery specs, and charging infrastructure — built with Python, Pandas, and Seaborn.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

</div>

---

## 📌 About

This repository contains an end-to-end mini project on the **Global Electric Vehicle Market (2026)** dataset, covering the full pipeline from raw data to an interactive dashboard:

1. **Data Cleaning** – Checking nulls, duplicates, and text consistency, then producing a cleaned CSV
2. **EDA** – Sales by country, region, vehicle type, and manufacturer; battery capacity vs. range trends
3. **Dashboard** – A Streamlit app with cascading filters (Region → Country) and live KPIs, charts, and a downloadable filtered dataset

---

## 🖼️ Dashboard Preview

**Full Dashboard Overview**

![EV Dashboard](./ev%20dashboard.png)

**EV Sales by Vehicle Type**

![Units Sold by Vehicle Type](./unit%20sold.png)

**Market Share by Vehicle Type**

![Market Share](./market%20share.png)

---

## 🗺️ Repository Structure

```
global-ev-market-dashboard/
│
├── 📄 app.py                                              # Streamlit dashboard application
├── 📄 analysis.ipynb                                      # EDA notebook: data quality checks, cleaning, exploratory charts
├── 📄 global_ev_market_charging_infrastructure_2026.csv   # Raw dataset
├── 📄 global_ev_market_cleaned.csv                        # Cleaned dataset used by the dashboard
├── 📄 requirements.txt                                    # Python dependencies
├── 🖼️ ev dashboard.png                                    # Screenshot: full dashboard overview
├── 🖼️ unit sold.png                                       # Screenshot: sales by vehicle type
├── 🖼️ market share.png                                    # Screenshot: market share by vehicle type
└── 📄 README.md
```

---

## ⚙️ Dashboard Features

**Sidebar filters**
- 🌍 Region (single-select, defaults to Asia)
- 🇨🇳 Country (cascades from the selected Region)
- 🏛️ Govt Incentives (All / Yes / No)

**KPI summary**
- Total EV units sold
- Vehicle types covered
- Top-selling brand
- Average battery capacity / range

**Visualizations**
- EV sales by vehicle type, for the selected country
- EV sales by region, with the selected region highlighted
- Market share by vehicle type (pie chart)
- Top manufacturers by sales
- Battery capacity vs. vehicle range (scatter, colored by vehicle type)

**Data view**
- Filtered data table
- CSV download button for the current selection

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python** | Core language |
| 🐼 **Pandas** | Data wrangling and analysis |
| 📓 **Jupyter Notebook** | EDA and data cleaning workflow |
| 📊 **Matplotlib / Seaborn** | Data visualisation |
| 🚀 **Streamlit** | Interactive dashboard |

---

## ▶️ Run Locally

```bash
git clone https://github.com/amit-0333/global-ev-market-dashboard.git
cd global-ev-market-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## 👨‍💻 Author

**Amit Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-amit--0333-181717?style=flat&logo=github)](https://github.com/amit-0333)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/amit-kumar-a62a3640a/)

---

<div align="center">

> 📝 *Built as part of my Data Science and Python learning journey.*

⭐ **Star this repo if you found it useful!**

</div>
