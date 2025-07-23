import streamlit as st
from utils.scheduler import run_scheduler
import pandas as pd
import os

st.set_page_config(page_title="Smart Production Scheduler", layout="wide")
st.title("🧠 Smart Production Scheduler")

st.markdown("""
Upload order, machine, and material data to generate an optimized production schedule under resource constraints.
""")

# Upload files
orders_file = st.file_uploader("Upload Orders CSV", type="csv")
machines_file = st.file_uploader("Upload Machines CSV", type="csv")
materials_file = st.file_uploader("Upload Materials CSV", type="csv")

if orders_file and machines_file and materials_file:
    orders_df = pd.read_csv(orders_file)
    machines_df = pd.read_csv(machines_file)
    materials_df = pd.read_csv(materials_file)

    st.success("✅ Files uploaded successfully!")

    schedule_df, summary = run_scheduler(orders_df, machines_df, materials_df)

    st.subheader("📋 Optimized Production Schedule")
    st.dataframe(schedule_df)

    st.subheader("📊 Summary")
    for key, value in summary.items():
        st.metric(label=key, value=value)
