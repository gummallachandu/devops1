import streamlit as st
import tempfile
from crewai import Crew, Process
from tasks import read_requirements, create_jira_stories
from agents import ba_agent

st.title("SDLC POC: Upload Requirements and Create Jira Stories")

uploaded_file = st.file_uploader("Choose a requirements .txt file", type="txt")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Step 1: Define tasks
    read_task = read_requirements(tmp_path)
    create_task = create_jira_stories(read_task)

    # Step 2: Run Crew
    crew = Crew(
        agents=[ba_agent],
        tasks=[read_task, create_task],
        process=Process.sequential
    )
    crew.kickoff()

    # Step 3: Access outputs
    requirements_text = getattr(read_task.output, "raw", "")
    jira_results = getattr(create_task.output, "raw", "")

    st.subheader("Extracted Requirements")
    st.text(requirements_text)

    st.subheader("Jira Story Creation Results")
    st.write(jira_results)
