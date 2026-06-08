import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration

st.set_page_config(
page_title="Smart Manufacturing Cost & ROI Estimator",
page_icon="🏭",
layout="wide"
)

# Custom Styling

st.markdown("""

<style>
.stApp {
    background: linear-gradient(135deg, #E3F2FD, #F3E5F5);
}

div[data-testid="metric-container"] {
    background-color: white;
    border-radius: 15px;
    padding: 10px;
    border: 1px solid #d0d0d0;
}

.team-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border: 2px solid #1565C0;
}
</style>

""", unsafe_allow_html=True)

# Header

st.markdown("""

<div style="
background: linear-gradient(90deg,#1565C0,#7B1FA2);
padding:25px;
border-radius:15px;
text-align:center;
color:white;">
<h1>🏭 Smart Manufacturing Cost & ROI Estimator</h1>
<h3>ICT in Financial Technology (FinTech)</h3>
<p>Professional Manufacturing Financial Analytics Dashboard</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# Sidebar

with st.sidebar:
st.title("📊 FinTech Dashboard")

```
st.info(
    "Analyze manufacturing cost, revenue, profit and ROI."
)

st.markdown("### Features")
st.write("✅ Cost Estimation")
st.write("✅ Revenue Forecasting")
st.write("✅ Profit Analysis")
st.write("✅ ROI Calculation")
st.write("✅ Financial Dashboard")
```

# Inputs

st.header("📥 Manufacturing Inputs")

col1, col2 = st.columns(2)

with col1:
material_cost = st.number_input(
"Raw Material Cost ($)",
min_value=0.0,
value=5000.0
)

```
labor_cost = st.number_input(
    "Labor Cost ($)",
    min_value=0.0,
    value=3000.0
)

overhead_cost = st.number_input(
    "Overhead Cost ($)",
    min_value=0.0,
    value=2000.0
)
```

with col2:
units_produced = st.number_input(
"Units Produced",
min_value=1,
value=1000
)

```
selling_price = st.number_input(
    "Selling Price Per Unit ($)",
    min_value=0.0,
    value=15.0
)

investment = st.number_input(
    "Initial Investment ($)",
    min_value=1.0,
    value=15000.0
)
```

# Calculations

total_cost = material_cost + labor_cost + overhead_cost
revenue = units_produced * selling_price
profit = revenue - total_cost
cost_per_unit = total_cost / units_produced
roi = (profit / investment) * 100

if revenue > 0:
profit_margin = (profit / revenue) * 100
else:
profit_margin = 0

st.markdown("---")

# KPI Dashboard

st.header("📊 Financial Dashboard")

k1, k2, k3, k4, k5 = st.columns(5)

k1.metric("Total Cost", f"${total_cost:,.2f}")
k2.metric("Revenue", f"${revenue:,.2f}")
k3.metric("Profit", f"${profit:,.2f}")
k4.metric("Cost/Unit", f"${cost_per_unit:.2f}")
k5.metric("ROI", f"{roi:.2f}%")

st.markdown("---")

# Charts

c1, c2 = st.columns(2)

with c1:
st.subheader("🥧 Cost Breakdown")

```
fig1, ax1 = plt.subplots()

ax1.pie(
    [material_cost, labor_cost, overhead_cost],
    labels=["Material", "Labor", "Overhead"],
    autopct="%1.1f%%"
)

ax1.axis("equal")
st.pyplot(fig1)
```

with c2:
st.subheader("📈 Revenue vs Cost")

```
fig2, ax2 = plt.subplots()

categories = ["Cost", "Revenue", "Profit"]
values = [total_cost, revenue, profit]

ax2.bar(categories, values)

ax2.set_ylabel("Amount ($)")
ax2.set_title("Financial Performance")

st.pyplot(fig2)
```

st.markdown("---")

# Financial Insights

st.header("💡 Financial Insights")

st.metric(
"Profit Margin",
f"{profit_margin:.2f}%"
)

if roi >= 20:
st.success(
f"Excellent Investment Opportunity (ROI = {roi:.2f}%)"
)
elif roi >= 10:
st.info(
f"Good Investment Opportunity (ROI = {roi:.2f}%)"
)
else:
st.warning(
f"Low ROI ({roi:.2f}%). Consider reducing costs."
)

st.markdown("---")

# Summary Table

st.header("📋 Financial Summary")

summary = pd.DataFrame({
"Metric": [
"Material Cost",
"Labor Cost",
"Overhead Cost",
"Total Cost",
"Revenue",
"Profit",
"Cost Per Unit",
"Profit Margin (%)",
"ROI (%)"
],
"Value": [
material_cost,
labor_cost,
overhead_cost,
total_cost,
revenue,
profit,
cost_per_unit,
profit_margin,
roi
]
})

st.dataframe(summary, use_container_width=True)

st.markdown("---")

# Team Section

st.markdown("""

<div class="team-box">

<h2 style="text-align:center;color:#1565C0;">
👨‍💻 Project Team
</h2>

<ul style="font-size:18px;">
<li><b>Usman Ali Khan</b> — 25-ME-31</li>
<li><b>Umair Habib Usmani</b> — 25-ME-211</li>
<li><b>Zar Khan</b> — 25-ME-227</li>
<li><b>M. Junaid Ali</b> — 25-ME-63</li>
<li><b>Zohaib Rasheed</b> — 25-ME-215</li>
</ul>

<center>
<h3>Department of Mechanical Engineering</h3>
<h4>ICT in Financial Technology (FinTech)</h4>
</center>

</div>
""", unsafe_allow_html=True)
