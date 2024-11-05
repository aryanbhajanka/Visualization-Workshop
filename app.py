import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

# Set page configurations
st.set_page_config(page_title="Aesthetic Data Visualization", layout="centered")

# Custom CSS for styling and center alignment
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
st.markdown("<div class='markdown-text'>Section A, B.Tech CSE, 1st Semester</div>", unsafe_allow_html=True)
st.markdown("<div class='markdown-text'>RV University</div>", unsafe_allow_html=True)

# Dropdown Menu for Selecting Graph Type
st.markdown("<div class='header-text'>Select Graph Type</div>", unsafe_allow_html=True)
graph_type = st.selectbox("Choose a graph to display:", 
                          ("Bar Plot - Tips by Day", "Violin Plot - Tips by Gender", 
                           "Scatter Plot - Total Bill vs. Tip (Color-coded by Gender)",
                           "Box Plot - Distribution of Total Bill by Day (With Color by Time)",
                           "Histogram - Tip Distribution (With Color)"))

# Display selected graph
if graph_type == "Bar Plot - Tips by Day":
    st.plotly_chart(bar, use_container_width=True)
elif graph_type == "Violin Plot - Tips by Gender":
    st.plotly_chart(violin, use_container_width=True)
elif graph_type == "Scatter Plot - Total Bill vs. Tip (Color-coded by Gender)":
    st.plotly_chart(scatter, use_container_width=True)
elif graph_type == "Box Plot - Distribution of Total Bill by Day (With Color by Time)":
    st.plotly_chart(box, use_container_width=True)
elif graph_type == "Histogram - Tip Distribution (With Color)":
    st.plotly_chart(histogram, use_container_width=True)
