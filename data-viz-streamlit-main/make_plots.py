import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import seaborn as sns
import plotly.express as px
import altair as alt
from bokeh.plotting import figure


def matplotlib_plot(chart_type: str):
    """ return matplotlib plots """

    fig, ax = plt.subplots()
    if chart_type == "Data Missing Value Assessment":
        # with st.echo():
        st.image("Picture3.png")
    elif chart_type == "Numerical Analysis of The Data":
        st.image("Picture4.png")
    elif chart_type == "Different Data Analysis":
        st.image("Picture8.png")
        st.image("Picture9.png")
        st.image("Picture12.png")
    elif chart_type == "Tableau Data Visualization":
        st.image("Picture10.png")
        st.image("Picture11.png")
        # st.image("Picture15.png")
        # st.image("Picture16.png")
        st.image("Picture17.png")
        st.image("Picture18.png")

    return fig


def sns_plot(chart_type: str):
    """ return seaborn plots """

    fig, ax = plt.subplots()
    if chart_type == "Numerical Analysis of The Data":
        # with st.echo():
        st.image("Picture7.png")

    elif chart_type == "Different Data Analysis":
        st.image("Picture13.png")
        st.image("Picture14.png")
        st.image("Picture15.png")
        st.image("Picture16.png")

    elif chart_type == "Tableau Data Visualization":
        st.image("Picture19.png")
        st.image("Picture20.png")
        st.image("Picture21.png")

    return fig
