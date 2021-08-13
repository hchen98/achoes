import streamlit as st
import pandas as pd
import numpy as np



def search_df():
    temp_df = pd.DataFrame()
    col_list = st.session_state.df.columns.tolist()

    customAttriubutes_list = st.sidebar.multiselect("Select the attributes:", col_list)

    if len(customAttriubutes_list) > 0:
        for item in customAttriubutes_list:
            temp_df[item] = st.session_state.df[item]

        keyWrd = st.text_input("Enter the search term:")

        if len(keyWrd) > 0:
            for item in customAttriubutes_list:
                filt = (st.session_state.df[item] == keyWrd)
                temp_df = st.session_state.df.loc[filt]

        st.dataframe(temp_df)
    


def search_seraies():
    st.write("Coming soon!")


def display_search():
    selectbox3 = st.sidebar.selectbox(
        "What dataset info you want to search?",
        ("DF", "Series")
        )
    
    OPTIONS = {
        "DF": search_df,
        "Series": search_seraies
    }

    OPTIONS[selectbox3]()