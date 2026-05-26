import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="R Sandeep & Associates",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit branding
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read and display the HTML file
def load_html_file():
    html_file_path = os.path.join(os.path.dirname(__file__), "index.html")
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        st.error(f"HTML file not found at {html_file_path}")
        return None

# Load and display HTML
html_content = load_html_file()
if html_content:
    st.components.v1.html(html_content, height=2000, scrolling=True)
