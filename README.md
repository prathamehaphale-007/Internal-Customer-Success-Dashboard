# 📊 ClearQuote Internal Customer Success Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)  
![Pandas](https://img.shields.io/badge/Data-Pandas-green)  
![Plotly](https://img.shields.io/badge/Visualization-Plotly-orange)

> A centralized Customer Success dashboard built to replace fragmented spreadsheet-based workflows. This application consolidates customer health, usage metrics, support activity, and fleet insights into a single interactive interface.

---

# 🎥 Video Demonstration

▶️ **Loom Walkthrough:** https://www.loom.com/share/92ffc9ef4d8744e1a315209b445425a2

---

# 🎯 Product Requirements Document (PRD)

## 1. Problem Statement
The Customer Success team currently relies on multiple spreadsheets and manual reports to track customer data. This creates inefficiencies, inconsistent insights, and poor visibility into customer health.

**Goal:** Build a centralized dashboard to monitor customer performance, usage trends, and support activity in one place.

---

## 2. User Personas

### Customer Success Manager (Primary User)
- Prepares for customer meetings  
- Tracks product usage and adoption  
- Monitors unresolved support tickets  

### Head of Customer Success (Secondary User)
- Reviews overall business performance  
- Tracks revenue (MRR) and customer distribution  
- Identifies risks and growth opportunities  

---

## 3. Requirements & Prioritization

### P0 (Must Have)
- Multi-tab dashboard  
- Integrated data across customers, usage, tickets, fleet  
- Filters and search  
- Actionable support tracking  

### P1 (Should Have)
- KPI cards (MRR, active customers, CSAT)  
- Map visualization  

### P2 (Nice to Have)
- Google SSO  
- Real-time data integration  

---

# 📊 Dataset Overview

### Customers
- Name, Tier, Status, MRR, CSM, Location  

### Usage
- Monthly inspections  
- Damage rates  
- API usage  
- Active drivers  

### Tickets
- Status, Priority  
- Channel  
- CSAT  
- Aging  

### Fleet
- Vehicle types  
- Telematics provider  
- FMS platform  
- Fleet age  

---

# 🧱 Data Model

All datasets are linked using:

customer_id

---

# 🖥️ Dashboard Features

## Tab 1: Customer Overview
- Customer table (Name, Tier, Status, MRR, CSM)  
- Filters: Tier, Status  
- Search by name  
- KPI Cards:
  - Total MRR  
  - Active Customers  
- Map visualization using location data  

---

## Tab 2: Usage Metrics
- Line charts:
  - Inspections  
  - API usage  
  - Damage rate  
- Customer filter (global / individual)  

---

## Tab 3: Support & Comms
- Ticket table (only active tickets)  
- Filters: Priority, Status  
- KPIs:
  - Open tickets  
  - Avg CSAT  
- Aging calculation (days open)  

---

## Tab 4: Fleet Distribution
- Vehicle type breakdown  
- Telematics provider distribution  
- FMS platform usage  
- Average fleet age  

---

# 📈 Key Design Decisions

### Actionable Data Focus
Only relevant, active information is shown to reduce noise.

### Dual-Level Insights
Supports both:
- High-level overview  
- Customer-level drill-down  

### Fast Development
Streamlit used to prioritize speed and clarity over complex architecture.

---

# 🛠️ Tech Stack

| Tool | Purpose |
|------|--------|
| Python | Core logic |
| Streamlit | Dashboard UI |
| Pandas | Data processing |
| Plotly | Visualization |
| openpyxl | Excel reading |

---

# 🏗️ Architecture

Excel → Pandas → Processing → Streamlit → Visualization

---

# 📁 Project Structure

clearquote-dashboard/  
│  
├── app.py  
├── data/  
│   ├── customers.xlsx  
│   ├── usage.xlsx  
│   ├── tickets.xlsx  
│   ├── fleet.xlsx  
│  
├── utils.py  
├── requirements.txt  
└── README.md  

---

# 💻 Sample Starter Code

```python
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("ClearQuote CS Dashboard")

customers = pd.read_excel("data/customers.xlsx")

tab = st.sidebar.radio("Navigation", [
    "Customer Overview",
    "Usage Metrics",
    "Support & Comms",
    "Fleet Distribution"
])

if tab == "Customer Overview":
    st.dataframe(customers)
```

---

# 🚀 How to Run

```bash
pip install streamlit pandas plotly openpyxl
streamlit run app.py
```

---

# 🔮 Future Improvements

- Google SSO authentication  
- Live database integration  
- Churn prediction models  
- Automated alerts for high-risk customers  

---

# 👨‍💻 Author

Prathmesh Aphale  
Product Analyst | SQL | Python | Power BI  
