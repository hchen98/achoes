import streamlit as st
import pandas as pd
import io
import numpy as np



def info():
    buffer = io.StringIO()
    st.session_state.df.info(buf=buffer)
    s = buffer.getvalue()

    st.text(s)


def describe():
    st.write(st.session_state.df.describe())


def missing_data():
    # check the missing val % in the dataset
    missing_values_count = st.session_state.df.isnull().sum()

    # how many total missing values do we have?
    total_cells = np.product(st.session_state.df.shape)
    total_missing = missing_values_count.sum()

    # percent of data that is missing
    percent_missing = (total_missing/total_cells) * 100
    st.write(f"Missing Data: {percent_missing} %")


def unique_value():
    temp_df = pd.DataFrame()
    col_list = st.session_state.df.columns.tolist()
    customAttriubutes_list = st.sidebar.multiselect("Select the attributes:", col_list)

    if customAttriubutes_list:
        for item in customAttriubutes_list:
            temp_df[item] = st.session_state.df[item].unique()

        st.dataframe(temp_df)


def unique_value_count():
    temp_df = pd.DataFrame()
    col_list = st.session_state.df.columns.tolist()
    customAttriubutes = st.sidebar.selectbox("Select the attributes:", col_list)

    if customAttriubutes:
        temp_df[customAttriubutes] = st.session_state.df[customAttriubutes].value_counts()

        st.dataframe(temp_df)


def display_data_info():
    selectbox3 = st.sidebar.selectbox(
        "What dataset info you want to see?",
        ("Info", "Describe", "Missing Data", "Series - Unique Value", "Series - Unique Value Count")
        )
    
    OPTIONS = {
        "Info": info,
        "Describe": describe,
        "Missing Data": missing_data,
        "Series - Unique Value": unique_value,
        "Series - Unique Value Count": unique_value_count,
    }

    OPTIONS[selectbox3]()