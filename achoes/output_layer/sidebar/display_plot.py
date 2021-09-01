import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px


def plot_bar():
    hue = None
    col_list = st.session_state.df.columns.tolist()

    x = st.sidebar.selectbox("X-axis", col_list)
    y = st.sidebar.selectbox("Y-axis", col_list)
    
    with st.expander("See explanation"):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)

    need_hue = st.sidebar.checkbox("Need key?", False)
    
    if need_hue:
        hue = st.sidebar.selectbox("Key", col_list)

    if x is not None and y is not None:
        fig = px.bar(st.session_state.df, x=x, y=y, color=hue)
        plt.title(str(x) + " VS " + str(y), size=15, weight='bold')
        plt.xlabel(str(x))
        plt.ylabel(str(y))
        st.plotly_chart(fig)


def plot_scatter():
    hue = None
    col_list = st.session_state.df.columns.tolist()

    x = st.sidebar.selectbox("X-axis", col_list)
    y = st.sidebar.selectbox("Y-axis", col_list)
        
    need_hue = st.sidebar.checkbox("Need key?", False)
    
    if need_hue:
        hue = st.sidebar.selectbox("Key", col_list)

    if x is not None and y is not None:
        fig = px.scatter(st.session_state.df, x=x, y=y, color=hue)
        plt.title(str(x) + " VS " + str(y), size=15, weight='bold')
        plt.xlabel(str(x))
        plt.ylabel(str(y))
        st.plotly_chart(fig)


def plot_pie():
    hue = None
    col_list = st.session_state.df.columns.tolist()

    col = st.sidebar.selectbox("Columns", col_list)

    need_hue = st.sidebar.checkbox("Need key?", False)
    
    if need_hue:
        hue = st.sidebar.selectbox("Key", col_list)

    if col is not None:
        fig = px.pie(st.session_state.df, values=col, names=hue)
        plt.title(str(col), size=15, weight='bold')
        st.plotly_chart(fig)


def pair_plot():
    fig = px.scatter_matrix(st.session_state.df)
    st.plotly_chart(fig)


def display_plot():
    selectbox4 = st.sidebar.selectbox(
        "What plot you want to see?",
        ("Bar", "Scatter", "Pie", "Pair Plot")
        )
    
    OPTIONS = {
        "Bar": plot_bar,
        "Scatter": plot_scatter,
        "Pie": plot_pie,
        "Pair Plot": pair_plot,
    }

    OPTIONS[selectbox4]()