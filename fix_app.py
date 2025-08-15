import streamlit as st
import time

st.title("🔬 Quick Test - Writing Assistant")

synthesis = """This is test content for writing assistant."""

col1, col2 = st.columns([1, 1])

with col1:
    writing_style = st.selectbox("Writing Style:", ["simple", "undergraduate"])
    
    if st.button("Transform Style"):
        st.success("Style transformed!")
        st.write("**Simple Style:** Easy to understand version...")

with col2:
    output_format = st.selectbox("Format:", ["Literature Review", "Executive Summary"])
    
    if st.button("Generate Format"):
        if output_format == "Literature Review":
            st.write("**Literature Review:** Academic literature review format...")
        else:
            st.write("**Executive Summary:** Key points for decision makers...")
