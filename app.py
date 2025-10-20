import streamlit as st
from Pages import welcome_page, team_page, project_overview_page, eda_page, model_comparison_page

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Welcome",
    "Team",
    "Project Overview",
    "EDA",
    "Model Comparison"
])

# --- Render Pages ---
if page == "Welcome":
    welcome_page.show()
elif page == "Team":
    team_page.show()
elif page == "Project Overview":
    project_overview_page.show()
elif page == "EDA":
    eda_page.show()
elif page == "Model Comparison":
    model_comparison_page.show()
