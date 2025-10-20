import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.title("Project Overview 📰📊")

    # --- Project Description ---
    st.subheader("Project Description")
    st.write("""
    This project analyzes a dataset of news articles across various domains:
    Business, Technology, Sports, Education.
    Objectives:
    - Understand dataset distribution
    - Train and evaluate multiple classification models
    - Compare model performance and identify the best model
    """)

    # --- Models Trained ---
    st.subheader("Models Trained")
    st.write("""
    - Logistic Regression  
    - Random Forest  
    - Linear SVM  
    - Multinomial Naive Bayes  
    - CatBoost Classifier
    """)

    # --- Placeholder Model Performance ---
    results_df = pd.DataFrame({
        "Model": ["Logistic Regression", "Random Forest", "Linear SVM", "Multinomial NB", "CatBoost"],
        "Accuracy": [0.9855, 0.9737, 0.9873, 0.9837, 0.9782],
        "F1_Score": [0.984, 0.972, 0.986, 0.982, 0.977]
    })

    best_model = results_df.loc[results_df['Accuracy'].idxmax(), 'Model']
    best_acc = results_df['Accuracy'].max()

    st.subheader("Best Model")
    st.info(f"**{best_model}** → Accuracy: {best_acc*100:.2f}%")

    st.subheader("Model Performance Table")
    st.dataframe(results_df)

    st.subheader("Model Accuracy Comparison")
    plt.figure(figsize=(8,5))
    colors = ['gold' if model == best_model else 'lightblue' for model in results_df['Model']]
    sns.barplot(x='Model', y='Accuracy', data=results_df, palette=colors)
    plt.title(f'Model Accuracy (Best: {best_model})')
    plt.ylim(0,1)
    plt.xticks(rotation=15)
    st.pyplot(plt)
