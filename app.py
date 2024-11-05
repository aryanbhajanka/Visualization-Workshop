import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

tips = sns.load_dataset('tips')
tips.head()

fig1 = px.bar(tips, x="day", y="tip")

fig2 = px.violin(tips, x="sex", y="tip")

st.title("Data Visualization with Plotly")

st.header("Plot 1: Bar Plot - Tips by Day")
st.plotly_chart(fig1)
st.markdown('''**Insight Observed**: (Add your insights here)''')

st.header("Plot 2: Violin Plot - Tips by Gender")
st.plotly_chart(fig2)
st.markdown('''**Insight Observed**: (Add your insights here)''')