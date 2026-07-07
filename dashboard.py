import streamlit as st
import pandas as pd
from datetime import datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake

if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

if not st.session_state.tracker_started:
    st.title("Welcome to AI Water Tracker")
    st.markdown("""
        Track your daily hydration with help of AI assistant.
        Log your intake, get smart feedback and stay healthy effortlessly.
    """)

    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.rerun()

else:
    st.sidebar.header("Log Your Water Intake")

    user_id = st.sidebar.text_input("User ID", value="user_123")
    intake_ml = st.sidebar.number_input("Water Intake (ml)", min_value=0, step=100)

    if st.sidebar.button("Submit"):
        if user_id and intake_ml:
            log_intake(user_id, intake_ml)
            st.success(f"Logged {intake_ml} ml for {user_id}")

            agent = WaterIntakeAgent()
            feedback = agent.analyze_intake(intake_ml)

            st.info(f"AI Feedback: {feedback}")