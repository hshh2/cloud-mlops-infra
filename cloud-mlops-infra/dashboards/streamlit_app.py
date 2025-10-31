import streamlit as st
import mlflow
import pandas as pd

st.title("Cloud ML Training Dashboard")

runs = mlflow.search_runs()
st.dataframe(runs[['run_id', 'params.model_name', 'metrics.accuracy', 'start_time']])
