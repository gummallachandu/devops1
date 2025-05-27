from crewai.tools import BaseTool
from pydantic import BaseModel, Field, PrivateAttr
from typing import Type
import os
import requests
from requests.auth import HTTPBasicAuth
import json

# --- File reading tool ---

class FileReadInput(BaseModel):
    file_path: str = Field(..., description="Path to the .txt file to read")

class FileReadTool(BaseTool):
    name: str = "file_read"
    description: str = "Reads content from a .txt file, returning text."
    args_schema: Type[BaseModel] = FileReadInput

    def _run(self, file_path: str) -> str:
        if not file_path or not os.path.exists(file_path):
            return "File not found."
        if not file_path.endswith(".txt"):
            return "Only .txt files are supported."
        with open(file_path, "r") as f:
            return f.read()

    async def _arun(self, file_path: str) -> str:
        raise NotImplementedError("Async not supported")

# --- Jira story creation tool ---

class JiraCreateStoryInput(BaseModel):
    summary: str = Field(..., description="Jira story summary")
    description: str = Field(..., description="Jira story description")

class JiraCreateStoryTool(BaseTool):
    name: str = "jira_create_story"
    description: str = "Creates a user story in Jira with specified summary and description."
    args_schema: Type[BaseModel] = JiraCreateStoryInput

    _jira_url: str = PrivateAttr()
    _jira_username: str = PrivateAttr()
    _jira_api_token: str = PrivateAttr()
    _project_key: str = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from dotenv import load_dotenv
        load_dotenv()
        self._jira_url = os.getenv("JIRA_INSTANCE_URL")
        self._jira_username = os.getenv("JIRA_USERNAME")
        self._jira_api_token = os.getenv("JIRA_API_TOKEN")
        self._project_key = os.getenv("JIRA_PROJECT_KEY", "SDLC")

    def _run(self, summary: str, description: str) -> str:
        # Convert plain text description to Atlassian Document Format (ADF)
        adf_description = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {"type": "text", "text": description}
                    ]
                }
            ]
        }
        payload = {
            "fields": {
                "project": {"key": self._project_key},
                "summary": summary,
                "description": adf_description,
                "issuetype": {"name": "Story"}
            }
        }
        api_endpoint = f"{self._jira_url}/rest/api/3/issue"
        response = requests.post(
            api_endpoint,
            headers={"Content-Type": "application/json"},
            auth=HTTPBasicAuth(self._jira_username, self._jira_api_token),
            data=json.dumps(payload)
        )
        if response.status_code == 201:
            return response.json().get("key", "Unknown issue key")
        return f"Failed to create ticket: {response.text}"

    async def _arun(self, summary: str, description: str) -> str:
        raise NotImplementedError("Async not supported")
