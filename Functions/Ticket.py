import requests
from requests.auth import HTTPBasicAuth
import json

from configparser import ConfigParser

config = ConfigParser()

config.read("./.env")

def createSubTask(parentIssueKey, scheduleTime, serverName):
    try: 

        jira_url = config.get("JIRA", "URL")
        email = config.get("JIRA", "USERNAME")
        api_token = config.get("JIRA", "API_KEY").strip('"')
        project_key = config.get("JIRA", "PROJECT_KEY")

        subtaskData = {
            "fields": {
                "project": {"key": project_key},
                "summary": f"Automox Manual Patching - {scheduleTime} - {serverName}",
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {"type": "paragraph", "content": [{"type": "text", "text": ""}]}
                    ],
                },
                "issuetype": {"name": "Sub-task"},
                "parent": {"key": parentIssueKey},
            }
        }

        url = f"{jira_url}/rest/api/3/issue"

        response = requests.post(
            url,
            data=json.dumps(subtaskData),
            auth=HTTPBasicAuth(email, api_token),
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 201:
            print(f"INFO: Subtask created successfully for {serverName} - Issue Key: {response.json()['key']}")
        else:
            print(f"Failed to create subtask: {response.status_code}, {response.text}")

    except Exception as e:
        print(f"ERROR: Failed to create subtasks - {e}")
