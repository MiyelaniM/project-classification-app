import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def show():
    st.title("Project Overview 📰📊")

    # --- Project Description ---
    st.subheader("Project Description")
    st.write("""
    This project involves analyzing a dataset of news articles across multiple domains.
    Objectives:
    - Understand the distribution of articles
    - Train multiple classification models
    - Compare performance and select best model
    """)

    # --- Models Trained ---
    st.subheader("Models Trained")
    st.write("""
    - Logistic Regression
    - Random Forest Classifier
    - Linear SVM
    - Multinomial Naive Bayes
    - CatBoost Classifier
    """)

    # --- Graphs from Notebook ---
    st.subheader("Model Accuracy Comparison")

    # Option 1: Show saved image
    try:
        img = Image.open("model_accuracy.png")  # image saved from notebook
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.write("No saved image found, displaying figure directly.")

        # Option 2: Generate figure directly in Streamlit
        data = {
            "Model": ["Logistic Regression", "Random Forest", "Linear SVM", "Multinomial NB", "CatBoost"],
            "Accuracy": [0.9855, 0.9737, 0.9873, 0.9837, 0.9783]
        }
        results_df = pd.DataFrame(data)

        fig, ax = plt.subplots(figsize=(7, 4))
        sns.barplot(x='Model', y='Accuracy', data=results_df, palette='viridis', ax=ax)
        ax.set_ylim(0, 1)
        ax.set_title("Model Accuracy Comparison")
        st.pyplot(fig)
