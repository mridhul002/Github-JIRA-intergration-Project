from flask import Flask , request
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'] )
def createJIRA():
    data = request.get_json()

    # Example for GitHub issue comment body
    body = data.get("comment", {}).get("body", "").strip()

    url = "https://projectdemo.atlassian.net//rest/api/3/issue"

    API_TOKEN = "..gyV6sH3rlGJVObKxcIexoAKcVyMFyg906smw-kBb0X7CzM-xOHxJeN7Fx5ppUHuWssG66HMHMt_..." #your API token

    auth = HTTPBasicAuth("mail@gmail.com", API_TOKEN )


    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {

        "description": {
        "content": [
            {
            "content": [
                {
                "text": "MY first issue .",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },

        "issuetype": {
            "id": "10041"
        },
    
        "project": {
            "key": "FP"
        },
        "summary": "do it fast",
    },
    "update": {}
    } )

    if body == "/jira":
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return {"message": "No /jira keyword found. Skipping Jira creation."}, 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)    
