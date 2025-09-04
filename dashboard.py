import streamlit as st

LOG_PATH = "logs/fall_events.log"

st.title("🧓 Fall Detection Dashboard")
st.subheader("Fall History")

try:
    with open(LOG_PATH, "r") as log_file:
        logs = log_file.readlines()
        for entry in logs:
            st.write(f"🕒 {entry.strip()}")
except FileNotFoundError:
    st.warning("No fall events logged yet.")