import streamlit as st

from core.file_handling import csv

from core.output_layer.sidebar import display_df
from core.output_layer.sidebar import display_data_info
from core.output_layer.sidebar import display_plot
from core.output_layer.sidebar import display_modify
from core.output_layer.sidebar import display_search

if __name__ == "__main__":

    st.title("Data Exploring Tool - Version 0.0.1")

    uploaded_files = st.file_uploader("Upload CSV", type=['csv'])
    
    if uploaded_files is not None:
        st.session_state.df = csv.pre_read_csv(uploaded_files)
        st.write("Dataframe loaded")
        
        if 'df' not in st.session_state:
            st.session_state.df = st.session_state.df
            st.write("DF wrote to session")

        # load the first sidebar
        selectbox1 = st.sidebar.selectbox(
        "What would you want to do?",
        ("Display DF", "Show Data Info", "Search", "Plot Dataset", "Modify")
        )

        ACTION = {
            "Display DF": display_df.display_df,
            "Show Data Info": display_data_info.display_data_info,
            "Search": display_search.display_search,
            "Plot Dataset": display_plot.display_plot,
            "Modify": display_modify.display_modify
        }

        # switch to the second sidebar
        # pass down the df
        act = ACTION[selectbox1]()
        
        
            

        