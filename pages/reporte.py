import streamlit as st
from fpdf import FPDF
import base64

report_text = st.text_input("Report Text")


export_as_pdf = st.button("Export Report")



if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, report_text)
    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)
