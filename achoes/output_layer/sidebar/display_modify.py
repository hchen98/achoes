import streamlit as st
import pandas as pd
import io

from achoes.components.modify import modify


def data_type():
    type_list = ("bool", "category", "float", "int", "int32", "int64", "object")
    col_list = st.session_state.df.columns.tolist()

    st.sidebar.write("Select the attribute(s) and the associated data type:\n\ne.g. ((attribute, dtype), ...)")
    
    customAttriubutes_list = st.sidebar.multiselect("Select the attributes:", col_list)
    customType = st.sidebar.multiselect("Associate type:", type_list)

    submit = st.sidebar.button("Submit")

    # only apply once the user clicks submit
    if submit:
        # make sure equal lenth
        if len(customAttriubutes_list) == len(customType): 
            # form a tuple array
            tranInfo_list = zip(customAttriubutes_list, customType)
            
            st.session_state.df = modify.changeType(st.session_state.df, tranInfo_list)
            st.write(st.session_state.df)
        else:
            st.sidebar.error("The number of attributes and types should be equal!")

    buffer = io.StringIO()
    st.session_state.df.info(buf=buffer)
    s = buffer.getvalue()

    st.text(s)


def date_time():
    ...


def applying():
    ...


def display_modify():
    selectbox5 = st.sidebar.selectbox(
        "What do you want to modify?",
        ("Data type", "Date Time", "Apply")
        )
    
    OPTIONS = {
        "Data type": data_type,
        "Date Time": date_time,
        "Apply": applying
    }

    OPTIONS[selectbox5]()