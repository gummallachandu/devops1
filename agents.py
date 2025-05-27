from crewai import Agent
from tools import FileReadTool, JiraCreateStoryTool

file_read_tool = FileReadTool()
jira_create_tool = JiraCreateStoryTool()

ba_agent = Agent(
    role="Business Analyst",
    goal=(
        "Read requirements from .txt files, break them down into well-structured Jira user stories. "
        "Each story should have a clear summary, background, acceptance criteria, and technical details. "
        "Ensure stories are actionable and unambiguous for developers and testers."
    ),
    backstory=(
        "A detail-oriented business analyst with strong Agile experience, "
        "skilled at translating requirements into clear, testable Jira tickets. "
        "Ensures each ticket includes a concise summary, detailed description, acceptance criteria, "
        "and relevant labels or components."
    ),
    tools=[file_read_tool, jira_create_tool],
    verbose=True,
    memory=True,
    max_iterations=10,
    cache=True
)


