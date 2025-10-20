import streamlit as st

def show():
    st.title("Meet the Team 👩🏽‍💻👨🏾‍💻")

    st.subheader("Our Team Members")

    # Team members data
    team = [
        {
            "name": "Miyelani Mathebula",
            "role": "Credit Risk Analyst",
            "bio": "Handles risk analysis, strategy, and model evaluation."
        },
        {
            "name": "Lerato Sokufudumala",
            "role": "Credit Risk Analyst",
            "bio": "Handles risk analysis, strategy, and model evaluation."
        }
    ]

    # Display each team member
    for member in team:
        st.markdown(f"### {member['name']}")
        st.write(f"**Role:** {member['role']}")
        st.write(f"**Bio:** {member['bio']}")
        st.markdown("---")  # separator
