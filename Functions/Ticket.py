import requests
from requests.auth import HTTPBasicAuth
import json

def createSubTask(parentIssueKey, scheduleTime, serverName):
    try: 
        jira_url = "https://pasindub5gncomau.atlassian.net"
        email = "pasindub5gncomau@gmail.com" 
        api_token = "ATATT3xFfGF0nh336R7rdc0ELYkCqL-JbucZDPK9GUt_q6h74x-mxUKcztoWnn5IfYpZrhJpuGin31NSs4TE2gG28Ln0bmRTuZwe7UhOa2QAhw48MNQpykCAZt-dciFYF8I_nVejPYHnjsKQoRjGe6RsxsZYeGwH1JrHlzMTU1wdUfYQa-S4xbY=34739ECD"

        subtaskData = {
            "fields": {
                "project": {
                    "key": "SUP" 
                },
                "summary": f'Automox Manual Patching - {scheduleTime} - {serverName}',
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": ""
                                }
                            ]
                        }
                    ]
                },
                "issuetype": {
                    "name": "Sub-task"
                },
                "parent": {
                    "key": parentIssueKey
                }
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
