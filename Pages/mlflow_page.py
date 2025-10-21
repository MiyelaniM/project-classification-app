import streamlit as st
import mlflow
import pandas as pd

def show():
    st.title("🔗 Partner Models Comparison - MLflow")

    experiment_name = "Partner_Models_Comparison"

    try:
        # Get the experiment object
        experiment = mlflow.get_experiment_by_name(experiment_name)
        if experiment is None:
            st.error(f"No experiment found with name '{experiment_name}'.")
            return

        experiment_id = experiment.experiment_id
        st.write(f"Experiment ID: {experiment_id}")
        st.write(f"Experiment Name: {experiment_name}")

        # Get all runs for this experiment
        runs = mlflow.search_runs(experiment_ids=[experiment_id], order_by=["start_time DESC"])
        if runs.empty:
            st.info("No runs found for this experiment.")
            return

        # Display summary table of runs
        st.subheader("Runs Summary")
        st.dataframe(
            runs[['run_id', 'status', 'start_time', 'metrics.accuracy', 'metrics.f1_score']]
        )

        # Optional: let user select a run to see parameters
        st.subheader("Run Details")
        run_ids = runs['run_id'].tolist()
        selected_run_id = st.selectbox("Select a run to see parameters and metrics", run_ids)

        run_data = runs[runs['run_id'] == selected_run_id].iloc[0]
        st.write("### Parameters")
        st.json(run_data.filter(like='params.').to_dict())
        st.write("### Metrics")
        st.json(run_data.filter(like='metrics.').to_dict())

    except Exception as e:
        st.error(f"Error accessing MLflow: {e}")
