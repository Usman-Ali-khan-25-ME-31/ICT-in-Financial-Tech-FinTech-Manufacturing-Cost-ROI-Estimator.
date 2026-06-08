import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
page_title="Smart Manufacturing Cost & ROI Estimator",
page_icon="🏭",
layout="wide"
)

st.markdown("""

<style>
.stApp{
background: linear-gradient(135deg,#E3F2FD,#F3E5F5);
}

div[data-testid="metric-container"]{
background:white;
border-radius:15px;
padding:15px;
box-shadow:0px 4px 10px rgba(0,0,0,0.1);
}

.sidebar .sidebar-content{
background:#1565C0;
}

.team-box{
background:white;
padding:20px;
border-radius:15px;
border:2px solid #1565C0;
}

</style>

""", unsafe_allow_html=True)

# HEADER

st.markdown("""

<div style='background: linear-gradient(90deg,#1565C0,#7B1FA2);
padding:25px;
border-radius:20px;
text-align:center;
color:white;'>

<h1>🏭 Smart Manufacturing Cost & ROI Estimator</h1>
<h3>ICT in Financial Technology (FinTech)</h3>
<p>Professional Manufacturing Financial Analytics Dashboard</p>

</div>
""", unsafe_allow_html=True)

st.markdown("")

# SIDEBAR

with st.sidebar:
st.title("📊 FinTech Dashboard")

```
st.info(
    "Estimate manufacturing costs, revenue, profit and ROI."
)

st.markdown("### Features")
st.write("✅ Manufacturing Cost Analysis")
st.write("✅ Revenue Forecasting")
st.write("✅ Profit Calculation")
st.write("✅ ROI Analysis")
st.write("✅ Financial Dashboard")
```

# INPUTS

st.header("📥 Input Manufacturing Data")

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

# CALCULATIONS

total_cost = material_cost + labor_cost + overhead_cost
revenue = units_produced * selling_price
profit = revenue - total_cost
cost_per_unit = total_cost / units_produced
roi = (profit / investment) * 100
profit_margin = (profit / revenue) * 100 if revenue > 0 else 0

st.markdown("---")

# KPI DASHBOARD

st.header("📊 Financial Dashboard")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Cost", f"${total_cost:,.2f}")
c2.metric("Revenue", f"${revenue:,.2f}")
c3.metric("Profit", f"${profit:,.2f}")
c4.metric("Cost / Unit", f"${cost_per_unit:.2f}")
c5.metric("ROI", f"{roi:.2f}%")

st.markdown("---")

# CHARTS

chart1, chart2 = st.columns(2)

with chart1:
st.subheader("🥧 Cost Breakdown")

```
fig1, ax1 = plt.subplots(figsize=(5,5))

ax1.pie(
    [material_cost, labor_cost, overhead_cost],
    labels=["Material","Labor","Overhead"],
    autopct="%1.1f%%",
    startangle=90
)

ax1.axis("equal")
st.pyplot(fig1)
```

with chart2:
st.subheader("📈 Revenue vs Cost")

```
fig2, ax2 = plt.subplots(figsize=(6,5))

categories = ["Cost","Revenue","Profit"]
values = [total_cost,revenue,profit]

ax2.bar(categories, values)

ax2.set_ylabel("Amount ($)")
ax2.set_title("Financial Performance")

st.pyplot(fig2)
```

st.markdown("---")

# BUSINESS ANALYSIS

st.header("💡 Financial Insights")

st.metric("Profit Margin", f"{profit_margin:.2f}%")

if roi >= 20:
st.success(
f"Excellent Investment Opportunity. ROI = {roi:.2f}%"
)

elif roi >= 10:
st.info(
f"Good Investment Opportunity. ROI = {roi:.2f}%"
)

else:
st.warning(
f"ROI is Low ({roi:.2f}%). Consider reducing production costs."
)

# TABLE

st.markdown("---")

st.header("📋 Financial Summary")

summary = pd.DataFrame({
"Metric":[
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
"Value":[
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

# TEAM SECTION

st.markdown("---")

st.markdown("""

<div class='team-box'>

<h2 style='text-align:center;color:#1565C0;'>
👨‍💻 Project Team
</h2>

<table style='width:100%;font-size:18px;'>

<tr>
<td><b>Usman Ali Khan</b></td>
<td>25-ME-31</td>
</tr>

<tr>
<td><b>Umair Habib Usmani</b></td>
<td>25-ME-211</td>
</tr>

<tr>
<td><b>Zar Khan</b></td>
<td>25-ME-227</td>
</tr>

<tr>
<td><b>M. Junaid Ali</b></td>
<td>25-ME-63</td>
</tr>

<tr>
<td><b>Zohaib Rasheed</b></td>
<td>25-ME-215</td>
</tr>

</table>

<br>

<center>
<h3>Department of Mechanical Engineering</h3>
<h4>ICT in Financial Technology (FinTech)</h4>
</center>

</div>
""", unsafe_allow_html=True)
