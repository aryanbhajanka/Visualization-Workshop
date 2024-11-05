import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

tips = sns.load_dataset('tips')
tips.head()

bar = px.bar(tips, x="day", y="tip")

violin = px.violin(tips, x="sex", y="tip")

scatter = px.scatter(tips, y="total_bill", x="tip")

box = px.box(tips, y="total_bill", x="day")

histogram = px.histogram(tips, x="tip", color="sex")

st.title("Data Visualization with Plotly")

st.header("Plot 1: Bar Plot - Tips by Day")
st.plotly_chart(bar)
st.markdown('''**Insight Observed**: (Add your insights here)''')

st.header("Plot 2: Violin Plot - Tips by Gender")
st.plotly_chart(violin)
st.markdown('''**Insight Observed**: (Add your insights here)''')

st.header("Plot 3: Scatter Plot - Tips by Gender")
st.plotly_chart(scatter)
st.markdown('''**Insight Observed**: (Add your insights here)''')
