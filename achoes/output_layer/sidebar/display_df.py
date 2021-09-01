import streamlit as st
import pandas as pd


def head():
    st.write(st.session_state.df.head())


def tail():
    st.write(st.session_state.df.tail())


def all_df():
    st.write(st.session_state.df)


def custom_attributes():
    temp_df = pd.DataFrame()
    col_list = st.session_state.df.columns.tolist()
    customAttriubutes_list = st.sidebar.multiselect("Select the attributes:", col_list)

    if customAttriubutes_list:
        for item in customAttriubutes_list:
            temp_df[item] = st.session_state.df[item]

        st.write(temp_df)


def random_df():
    n = st.sidebar.number_input("Input the sameple size", 
    min_value=0, max_value=len(st.session_state.df.iloc[:]), step=1)
    if n:
        st.write(st.session_state.df.sample(int(n)))


def display_df():
    selectbox2 = st.sidebar.selectbox(
        "What DF you want to print?",
        ("Head", "Tail", "All DF", "Custom Attributes (manual input)", "Sample")
        )
    
    OPTION = {
        "Head": head,
        "Tail": tail,
        "All DF": all_df,
        "Custom Attributes (manual input)": custom_attributes,
        "Sample": random_df
    }

    OPTION[selectbox2]()

