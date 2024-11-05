import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

# Set page configurations
st.set_page_config(page_title="Aesthetic Data Visualization", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Page and background color */
        .stApp {
            background-color: #f5f7fa;
        }
        /* Title styling */
        .title-text {
            font-family: 'Verdana', sans-serif;
            color: #333333;
            font-size: 36px;
        }
        /* Header styling */
        .header-text {
            font-family: 'Verdana', sans-serif;
            color: #5c5c8a;
            font-size: 28px;
        }
        /* General text styling */
        .markdown-text {
            font-family: 'Arial', sans-serif;
            color: #444444;
        }
    </style>
""", unsafe_allow_html=True)

# Load and display dataset
tips = sns.load_dataset('tips')

# Custom color theme
color_theme = px.colors.qualitative.Pastel

# Define plots with consistent styling
bar = px.bar(tips, x="day", y="tip", color="day", color_discrete_sequence=color_theme, title="Tips by Day")
violin = px.violin(tips, x="sex", y="tip", color="sex", color_discrete_sequence=color_theme, title="Tips by Gender")
scatter = px.scatter(tips, x="tip", y="total_bill", color="sex", color_discrete_sequence=color_theme, title="Total Bill vs Tip (by Gender)")
box = px.box(tips, x="day", y="total_bill", color="time", color_discrete_sequence=color_theme, title="Total Bill by Day and Time")
histogram = px.histogram(tips, x="tip", color="sex", color_discrete_sequence=color_theme, title="Tip Distribution by Gender")

# App Title
st.markdown("<div class='title-text'>Data Visualization with Plotly</div>", unsafe_allow_html=True)
st.markdown("<div class='markdown-text'>Created By: Aryan Bhajanka</div>", unsafe_allow_html=True)

# Display plots with custom headers
st.markdown("<div class='header-text'>Plot 1: Bar Plot - Tips by Day</div>", unsafe_allow_html=True)
st.plotly_chart(bar)

st.markdown("<div class='header-text'>Plot 2: Violin Plot - Tips by Gender</div>", unsafe_allow_html=True)
st.plotly_chart(violin)

st.markdown("<div class='header-text'>Plot 3: Scatter Plot - Total Bill vs. Tip (Color-coded by Gender)</div>", unsafe_allow_html=True)
st.plotly_chart(scatter)

st.markdown("<div class='header-text'>Plot 4: Box Plot - Distribution of Total Bill by Day (With Color by Time)</div>", unsafe_allow_html=True)
st.plotly_chart(box)

st.markdown("<div class='header-text'>Plot 5: Histogram Plot - Tip Distribution (With Color)</div>", unsafe_allow_html=True)
st.plotly_chart(histogram)

# Option to view the dataset
st.markdown("<div class='header-text'>Dataset</div>", unsafe_allow_html=True)
if st.checkbox("Show Dataset"):
    st.dataframe(tips)
