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
            padding: 20px;
        }
        /* Title styling */
        .title-text {
            font-family: 'Verdana', sans-serif;
            color: #333333;
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Header styling */
        .header-text {
            font-family: 'Verdana', sans-serif;
            color: #5c5c8a;
            font-size: 28px;
            text-align: center;
            margin-top: 30px;
        }
        /* General text styling */
        .markdown-text {
            font-family: 'Arial', sans-serif;
            color: #444444;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Styling for plotly charts */
        .plot-container {
            display: flex;
            justify-content: center;
            padding: 10px;
        }
        .centered-dataframe {
            display: flex;
            justify-content: center;
            padding: 10px;
        }
        
    </style>
""", unsafe_allow_html=True)

# Load dataset
tips = sns.load_dataset('tips')

# Define a consistent color theme
color_theme = px.colors.qualitative.Pastel

# Define plots with consistent styling
bar = px.bar(tips, x="day", y="tip", color="day", color_discrete_sequence=color_theme, title="Tips by Day")
violin = px.violin(tips, x="sex", y="tip", color="sex", color_discrete_sequence=color_theme, title="Tips by Gender")
scatter = px.scatter(tips, x="tip", y="total_bill", color="sex", color_discrete_sequence=color_theme, title="Total Bill vs Tip (by Gender)")
box = px.box(tips, x="day", y="total_bill", color="time", color_discrete_sequence=color_theme, title="Total Bill by Day and Time")
histogram = px.histogram(tips, x="tip", color="sex", color_discrete_sequence=color_theme, title="Tip Distribution by Gender")

# App Title and Creator's Name
st.markdown("<div class='title-text'>Data Visualization with Plotly</div>", unsafe_allow_html=True)
st.markdown("<div class='markdown-text'>Created By: Aryan Bhajanka</div>", unsafe_allow_html=True)

# Dataset Toggle Section
st.markdown("<div class='header-text'>Dataset</div>", unsafe_allow_html=True)
st.markdown("<div class='centered-dataframe'>", unsafe_allow_html=True)
st.dataframe(tips)
st.markdown("</div>", unsafe_allow_html=True)

# Displaying plots in a structured layout with columns
st.markdown("<div class='header-text'>Visualizations</div>", unsafe_allow_html=True)

# Row 1: Bar Plot and Violin Plot
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='header-text'>Bar Plot - Tips by Day</div>", unsafe_allow_html=True)
    st.plotly_chart(bar, use_container_width=True)
with col2:
    st.markdown("<div class='header-text'>Violin Plot - Tips by Gender</div>", unsafe_allow_html=True)
    st.plotly_chart(violin, use_container_width=True)

# Row 2: Scatter Plot
st.markdown("<div class='header-text'>Scatter Plot - Total Bill vs Tip (Color-coded by Gender)</div>", unsafe_allow_html=True)
st.plotly_chart(scatter, use_container_width=True)

# Row 3: Box Plot and Histogram
col3, col4 = st.columns(2)
with col3:
    st.markdown("<div class='header-text'>Box Plot - Total Bill by Day (With Color by Time)</div>", unsafe_allow_html=True)
    st.plotly_chart(box, use_container_width=True)
with col4:
    st.markdown("<div class='header-text'>Histogram - Tip Distribution (Color-coded by Gender)</div>", unsafe_allow_html=True)
    st.plotly_chart(histogram, use_container_width=True)
