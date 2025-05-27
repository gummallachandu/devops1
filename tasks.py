from crewai import Task
from agents import ba_agent
from tools import FileReadTool, JiraCreateStoryTool

file_read_tool = FileReadTool()
jira_create_tool = JiraCreateStoryTool()

def read_requirements(file_path: str) -> Task:
    return Task(
        description=f"Read the .txt file from {file_path} using FileReadTool and return the content as text.",
        expected_output="Text content of the .txt file.",
        agent=ba_agent,
        tools=[file_read_tool],
        async_execution=False
    )

def create_jira_stories(read_task: Task) -> Task:
    return Task(
        description=(
            "Break down the requirements into clear, actionable Jira stories. "
            "For each story, provide: "
            "- A concise summary "
            "- A detailed description "
            "- Acceptance criteria "
            "- Suggested labels (UI, Backend, DevOps, etc.) "
            "Ensure each story is unambiguous, testable, and ready for developers."
        ),
        expected_output="List of well-structured Jira stories with summary, description, acceptance criteria, and labels.",
        agent=ba_agent,
        tools=[jira_create_tool],
        context=[read_task],
        async_execution=False,
        human_input=False
    )

