import streamlit as st
import mlflow
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("📊 Model Performance Insights")

    experiment_name = "Partner_Models_Comparison"

    # Fetch experiment
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        st.error(f"No experiment found with name '{experiment_name}'")
        return

    experiment_id = experiment.experiment_id

    # Get all runs
    runs = mlflow.search_runs(experiment_ids=[experiment_id], order_by=["start_time DESC"])
    if runs.empty:
        st.info("No runs found for this experiment.")
        return

    # Display summary table
    st.subheader("Runs Summary")
    st.dataframe(runs[['run_id', 'status', 'start_time', 'metrics.accuracy', 'metrics.f1_score']])

    # Show metrics comparison plots
    st.subheader("Performance Comparison")
    metrics_df = runs[['metrics.accuracy', 'metrics.f1_score']]
    
    fig, ax = plt.subplots()
    metrics_df.plot(kind='bar', ax=ax)
    ax.set_ylabel("Score")
    ax.set_xlabel("Run Index")
    ax.set_title("Accuracy & F1 Score per Run")
    st.pyplot(fig)

    # Show best performing run
    best_run = runs.loc[runs['metrics.accuracy'].idxmax()]
    st.subheader("Best Performing Run")
    st.write(f"Run ID: {best_run['run_id']}")
    st.write(f"Accuracy: {best_run['metrics.accuracy']:.4f}")
    st.write(f"F1 Score: {best_run['metrics.f1_score']:.4f}")

    # --- Notes Section ---
    st.subheader("Notes & Insights")
    st.markdown("""
    - The best model based on accuracy also has a strong F1 score, indicating a balanced performance on both classes.  
    - Models with lower accuracy tend to also have lower F1, suggesting consistent underperformance.  
    - Consider tuning hyperparameters or using ensemble methods to further improve results.  
    - For production, we might select the top 1–2 models and validate on a separate hold-out set.
    """)
