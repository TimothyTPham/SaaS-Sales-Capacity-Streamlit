import streamlit as st
import pandas as pd
import numpy as np

st.title("Sales Capacity & Pipeline Forecast Model")
st.write("""
This Streamlit app forecasts SaaS sales performance based on headcount growth and key sales assumptions.
""")

# Sidebar Inputs
starting_reps = st.sidebar.number_input("Starting Sales Reps", value=5)
monthly_hires = st.sidebar.number_input("Monthly Hires", value=2)
ramp_months = st.sidebar.number_input("Ramp Period (Months)", value=3)
quota = st.sidebar.number_input("Quota per Rep ($)", value=100000)
attainment = st.sidebar.slider("Attainment Rate (%)", 0, 100, 70) / 100
win_rate = st.sidebar.slider("Win Rate (%)", 0, 100, 25) / 100
sales_cycle = st.sidebar.number_input("Sales Cycle (Months)", value=1)
cac = st.sidebar.number_input("Customer Acquisition Cost (CAC $)", value=10000)
months = st.sidebar.slider("Forecast Horizon (Months)", 1, 36, 12)

# Initialize data storage
months_list = list(range(1, months + 1))
total_reps = []
fully_ramped_reps = []
bookings = []
pipeline_created = []
revenue = []
cac_payback_periods = []
arr = []

# Helper list to store hires by month
hires_by_month = [starting_reps] + [monthly_hires] * (months - 1)

for i in range(months):
    total = sum(hires_by_month[:i+1])
    total_reps.append(total)

    if i >= ramp_months:
        ramped = sum(hires_by_month[:i - ramp_months + 1])
    else:
        ramped = 0
    fully_ramped_reps.append(ramped)

    monthly_bookings = ramped * quota * attainment
    bookings.append(monthly_bookings)

    pipeline = monthly_bookings / win_rate if win_rate > 0 else 0
    pipeline_created.append(pipeline)

    if i >= sales_cycle:
        rev = bookings[i - sales_cycle]
    else:
        rev = 0
    revenue.append(rev)

    arr.append(monthly_bookings * 12)

    monthly_gross_profit = quota * attainment
    cac_payback = cac / monthly_gross_profit if monthly_gross_profit != 0 else np.nan
    cac_payback_periods.append(cac_payback)

# Create dataframe
forecast = pd.DataFrame({
    "Month": months_list,
    "Total Reps": total_reps,
    "Fully Ramped Reps": fully_ramped_reps,
    "Bookings ($)": bookings,
    "Pipeline Created ($)": pipeline_created,
    "Revenue ($)": revenue,
    "ARR ($)": arr,
    "CAC Payback Period (Months)": cac_payback_periods
})

# Display summary metrics
total_bookings = sum(bookings)
total_pipeline = sum(pipeline_created)
total_revenue = sum(revenue)
total_arr = arr[-1] if arr else 0

st.metric("Total Bookings", f"${total_bookings:,.0f}")
st.metric("Total Revenue", f"${total_revenue:,.0f}")
st.metric("Ending ARR", f"${total_arr:,.0f}")
st.metric("Total Pipeline", f"${total_pipeline:,.0f}")

# Display table
st.dataframe(forecast.style.format({
    "Bookings ($)": "${:,.0f}",
    "Pipeline Created ($)": "${:,.0f}",
    "Revenue ($)": "${:,.0f}",
    "ARR ($)": "${:,.0f}",
    "CAC Payback Period (Months)": "{:.1f}",
    "Total Reps": "{:,.0f}",
    "Fully Ramped Reps": "{:,.0f}"
}))

# Charts
st.line_chart(forecast.set_index("Month")["Bookings ($)"])
st.line_chart(forecast.set_index("Month")["ARR ($)"])

# Export
csv = forecast.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "sales_capacity_forecast.csv", "text/csv")
