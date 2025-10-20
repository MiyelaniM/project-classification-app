import streamlit as st
import pandas as pd

def show():
    st.title("Model Performance Overview 📊")

    # Model metrics from previous runs
    data = {
        "Model": ["Logistic Regression", "Random Forest", "Linear SVM", "Multinomial NB", "CatBoost"],
        "Accuracy": [0.9855, 0.9737, 0.9873, 0.9837, 0.9783],
        "Precision": [0.9856, 0.9741, 0.9873, 0.9837, 0.9786],
        "Recall": [0.9855, 0.9737, 0.9873, 0.9837, 0.9783],
        "F1-Score": [0.9855, 0.9738, 0.9873, 0.9837, 0.9783]
    }

    df_metrics = pd.DataFrame(data)

    # Highlight the best model
    best_model_index = df_metrics["Accuracy"].idxmax()

    st.subheader("All Models")
    st.dataframe(df_metrics.style.format("{:.4f}").apply(
        lambda x: ["background-color: lightgreen" if i == best_model_index else "" for i in x.index], axis=1
    ))

    # Show the best model explicitly
    st.subheader("Best Model")
    best_model = df_metrics.loc[best_model_index]
    st.write(f"**{best_model['Model']}** is the best model with:")
    st.write(f"- Accuracy: {best_model['Accuracy']:.4f}")
    st.write(f"- Precision: {best_model['Precision']:.4f}")
    st.write(f"- Recall: {best_model['Recall']:.4f}")
    st.write(f"- F1 Score: {best_model['F1-Score']:.4f}")

    st.write("---")
    st.write("✅ Note: These metrics are from the latest partner runs; no retraining is performed.")
