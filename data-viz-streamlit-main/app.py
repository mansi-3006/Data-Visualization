import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
from bokeh.plotting import figure
from make_plots import (
    matplotlib_plot,
    sns_plot,
)


# can only set this once, first thing to set
st.set_page_config(layout="wide")

plot_types = (
    "Data Missing Value Assessment",
    "Numerical Analysis of The Data",
    "Different Data Analysis",
    "Tableau Data Visualization"
)
libs = (
    "Matplotlib",
    "Seaborn",
)

# Top text area
with st.container():
    st.title("U.S Airbnb Data Visualization 📊")
    # st.header("Popular plots in popular plotting libraries")
    # st.subheader("""See the code and plots for six libraries at once!""")

# User choose type
chart_type = st.selectbox("Choose your chart type", plot_types)

with st.container():
    st.subheader(f"Showing:  {chart_type}")
    st.write("")

two_cols = st.checkbox("2 columns?", True)
if two_cols:
    col1, col2 = st.columns(2)


# create plots
def show_plot(kind: str):
    if kind == "Matplotlib":
        plot = matplotlib_plot(chart_type)
        # st.image("Picture9.png")
    elif kind == "Seaborn":
        plot = sns_plot(chart_type)
        # st.image("Picture9.png")


# output plots
if two_cols:
    with col1:
        show_plot(kind="Matplotlib")
    with col2:
        show_plot(kind="Seaborn")

else:
    with st.container():
        for lib in libs:
            show_plot(kind=lib)

# display data
with st.container():
    show_data = st.checkbox("See the raw data?")

    if show_data:
        df = pd.read_csv("AB_US_2020.csv")
        df

    # notes
    st.subheader("Notes")
    st.write(
        """
        - This app uses [Streamlit](https://streamlit.io/) and the [U.S Airbnb Dataset](https://www.kaggle.com/datasets/kritikseth/us-airbnb-open-data) dataset.
        - To see the full code check out the [GitHub repo](https://github.com/mansi-3006/Data-Visualization).
        - Since its inception in 2008, Airbnb has disrupted the traditional hospitality industry as more travellers decide to use Airbnb as their primary means of accommodation. Airbnb offers travellers a more unique and personalized way of accommodation and experience.
        - This dataset has one file- AB_US_2020.csv which has columns describing features such as host id, hostname, listing id, listing name, latitude and longitude of listing, the neighbourhood, price, room type, minimum number of nights, number of reviews, last review date, reviews per month, availability, host listings and city.
        - This dataset is a compilation of multiple datasets found on Inside Airbnb.
        """
    )
