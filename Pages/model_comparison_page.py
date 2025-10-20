import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.title("Model Comparison 📊")
    
    st.write("This page will show the comparison of all trained models.")
    
    # Example placeholder table
    results_df = pd.DataFrame({
        "Model": ["Logistic Regression", "Random Forest", "Linear SVM", "Multinomial NB", "CatBoost"],
        "Accuracy": [0.9855, 0.9737, 0.9873, 0.9837, 0.9782],
        "F1_Score": [0.984, 0.972, 0.986, 0.982, 0.977]
    })
    
    st.subheader("Model Performance Table")
    st.dataframe(results_df)

    st.subheader("Accuracy Comparison")
    best_model = results_df.loc[results_df['Accuracy'].idxmax(), 'Model']
    plt.figure(figsize=(8,5))
    colors = ['gold' if model == best_model else 'lightblue' for model in results_df['Model']]
    sns.barplot(x='Model', y='Accuracy', data=results_df, palette=colors)
    plt.title(f'Model Accuracy (Best: {best_model})')
    plt.ylim(0,1)
    plt.xticks(rotation=15)
    st.pyplot(plt)
