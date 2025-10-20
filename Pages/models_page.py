import streamlit as st
from PIL import Image
import os

def show():
    st.title("Model Comparison & Metrics 📈")

    st.subheader("Best Model")
    st.write("Linear SVM performed the best in our experiments.")

    st.subheader("Performance Visualizations")
    for file in ["model_accuracy.png", "confusion_matrix.png"]:
        if os.path.exists(file):
            img = Image.open(file)
            st.image(img, use_column_width=True)
        else:
            st.write(f"No saved image found: {file}")
