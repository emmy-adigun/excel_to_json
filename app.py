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


uploaded_file = st.sidebar.file_uploader("Choose a file" ,type=['xlsx'])
if uploaded_file:
    file_details = {
        "Filename":uploaded_file.name,
        "FileType":uploaded_file.type,
        "FileSize":uploaded_file.size}

    wb = openpyxl.load_workbook(uploaded_file)

    st.sidebar.subheader("File details:")
    st.sidebar.json(file_details,expanded=False)
    st.sidebar.markdown("----")

    ## Select sheet
    sheet_selector = st.sidebar.selectbox("Select sheet:",wb.sheetnames)     
    df = pd.read_excel(uploaded_file,sheet_selector)
    st.markdown(f"### Currently Selected: `{sheet_selector}`")
    st.write(df)

    ## Do something after a button
    doLogic_btn = st.button("➕")
    if doLogic_btn:
        df2 = df.sum().transpose()
        st.write(df2)

        # Do something more after the previous button
        # >> But this will fail because the button will go back to _False_ 
        # >> so nothing will be shown afterwards
        another_btn = st.checkbox("Another +")
        if another_btn:
            df3 = df2.sum()
            st.write(df3)
     # st.write(json_str)