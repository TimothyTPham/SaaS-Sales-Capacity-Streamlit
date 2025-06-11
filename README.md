# Sales Capacity Forecast Model

This is a simple and interactive SaaS sales capacity and pipeline forecast model built with [Streamlit](https://streamlit.io/). It helps early-stage startups project headcount growth, ramping productivity, quota-based bookings, and revenue over time.

![App Preview](https://raw.githubusercontent.com/TimothyTPham/SaaS-Sales-Capacity-Streamlit/main/preview.png)

## 📊 What's Included:
- Dynamic headcount planning
- Fully ramped rep logic
- Bookings forecast using quota and attainment
- Pipeline creation via win rate
- Revenue recognition based on sales cycle
- Interactive UI with charts and CSV export

## ⚙️ Key Assumptions (modifiable in-app):
- Starting Reps: 5  
- Monthly Hires: 2  
- Ramp Period: 3 months  
- Quota per Rep: $100,000  
- Attainment Rate: 70%  
- Win Rate: 25%  
- Sales Cycle: 1 month  
- Forecast Horizon: 12 months  

## 🔗 Live App:
[https://saas-sales-capacity-app-jkhdm84qdr9cfmt8qbx545.streamlit.app/](https://saas-sales-capacity-app-jkhdm84qdr9cfmt8qbx545.streamlit.app/)

## 📁 Try It Yourself:
Clone the repo and run locally:
```bash
pip install -r requirements.txt
streamlit run sales_capacity_model_app.py
