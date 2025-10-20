import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.title("Exploratory Data Analysis (EDA) 📊")

    # --- Dataset Overview ---
    st.subheader("Dataset Overview")
    st.write("Summary statistics, shape, missing values, etc.")

    # Example placeholder data
    df = pd.DataFrame({
        "Category": ["Business", "Technology", "Sports", "Education"]*25,
        "Length": [200, 300, 250, 220]*25
    })

    st.write("Dataset head:")
    st.dataframe(df.head())

    # --- Category Distribution ---
    st.subheader("Category Distribution")
    plt.figure(figsize=(6,4))
    sns.countplot(x="Category", data=df)
    plt.title("Articles per Category")
    st.pyplot(plt)

    # --- Article Length Distribution ---
    st.subheader("Article Length Distribution")
    plt.figure(figsize=(6,4))
    sns.histplot(df["Length"], bins=10)
    plt.title("Article Length")
    st.pyplot(plt)
