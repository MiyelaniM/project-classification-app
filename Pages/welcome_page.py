import streamlit as st

def show():
    st.title("Welcome to the News Classification Project 🚀📰")
    
    st.write("""
    This app allows you to:
    - Explore the dataset of news articles
    - See EDA (Exploratory Data Analysis)
    - View project overview and model performance
    - Compare different classification models
    - Learn which model performed the best
    """)

    st.subheader("Navigation Instructions")
    st.write("""
    Use the sidebar on the left to navigate between pages:
    - **Welcome:** You are here
    - **Team:** Meet the team members
    - **Project Overview:** See project objectives and models
    - **EDA:** Explore the dataset
    - **Model Comparison:** Compare model metrics
    """)
