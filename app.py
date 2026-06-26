import streamlit as st
from pipeline import run
import os

st.set_page_config(
    page_title="Business Data Analyzer",
    page_icon="📊"
)

st.title("📊 Business Data Analyzer")

st.write(
    "Upload a CSV or Excel file and generate an automatic report."
)

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully.")

    if st.button("Generate Report"):

        with st.spinner("Analyzing data..."):

            run(uploaded_file.name)

        st.success("Report generated successfully.")

        if os.path.exists("missing_values.png"):
            st.image(
                "missing_values.png",
                caption="Missing Values"
            )

        if os.path.exists("profit_by_category.png"):
            st.image(
                "profit_by_category.png",
                caption="Profit by Category"
            )

        if os.path.exists("report.pdf"):

            with open("report.pdf", "rb") as pdf:

                st.download_button(
                    label="Download PDF Report",
                    data=pdf,
                    file_name="report.pdf",
                    mime="application/pdf"
                )