import streamlit as st
import pandas as pd
import numpy as np

import openpyxl
# from wordcloud import WordCloud

st.set_page_config(layout="centered")

#st.title("Upload Excel File")
st.write("Upload Excel File")
st.write("Download a sample of the excel template to be uploaded. [link](https://iswtest.frb.io/skillbase/dynamic_certificate/uploads/training2.xls)")
st.markdown("""
<style>

.column-style {
    font-size:16px !important;
    text-align:left;
    color: rgb(61, 157, 243);
    border: 1px solid rgba(28, 131, 225, 0.1);
    background-color: rgba(28, 131, 225, 0.1);
    border-radius: 0.25rem;
    padding: 16px;
    opacity: 1;
}

</style>
""", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:


     # Can be used wherever a "file-like" object is accepted:
     excel_data_df = pd.read_excel(uploaded_file, skiprows=list(range(2)))
     json_str = excel_data_df.to_json('skillz.json', orient='records')
     
     st.markdown("#### **Check your download folder for the JSON file**")
     # st.write(json_str)