import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
# from wordcloud import WordCloud

st.set_page_config(layout="wide")

# st.title("Linkedin Connection Analysis")
st.write("Upload Excel File")

st.markdown("""
<style>
body{
       background: rgb(0, 23, 43);
       color: rgb(220, 220, 220);
}
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
.css-1njf6aq {
    background-color: blue;
    }
</style>
""", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Choose a file" ,type=['xlsx'])
if uploaded_file:
    file_details = {
        "Filename":uploaded_file.name,
        "FileType":uploaded_file.type,
        "FileSize":uploaded_file.size}

    wb = openpyxl.load_workbook(uploaded_file)

    json_str = wb.to_json('Products21.json', orient='records')
    st.markdown("### **Check your folder after upload**")
     # st.write(json_str)