# Github-JIRA-intergration-Project
This repo helps you to automation for create story in Jira when a issue in github

DESCRIPTION:
This project automates the process of creating a JIRA story whenever a specific command (/jira) is posted in a GitHub issue comment. It uses a Flask-based webhook receiver that listens for GitHub issue events, processes the comment body, and triggers JIRA's REST API to create a new story in the specified project. The integration eliminates the need for manual task creation in JIRA, ensuring faster workflow automation and improved collaboration between development and project management teams



⚙️ Setup Instructions
1️⃣ Clone the Repository

git clone https://github.com/your-username/Github-JIRA-Integration-Project.git
cd Github-JIRA-Integration-Project

2️⃣ Install Dependencies

pip install flask requests

3️⃣ Configure Environment Variables
Replace placeholders in the script with your own details:

API_TOKEN = "YOUR_JIRA_API_TOKEN"
auth = HTTPBasicAuth("YOUR_JIRA_EMAIL", API_TOKEN)

API Token: Generate from your Atlassian Account Settings.

Project Key: Replace "FP" in the payload with your JIRA project key.

Issue Type ID: Replace "10041" with the correct ID from your JIRA account.

🔗 Setting up GitHub Webhook
Go to your GitHub repository Settings → Webhooks.

Click "Add webhook".

Set Payload URL:
http://<YOUR_SERVER_PUBLIC_IP>:5000/createJIRA

Content type: application/json.

Select "Let me select individual events" → Check Issue comments.

Save the webhook.

▶️ Running the Flask Server
python app.py
Your Flask server will run on port 5000 and listen for GitHub events.

📌 How It Works
GitHub sends an issue comment event to your Flask endpoint.

The script extracts the comment body.

If the body contains /jira, it sends a POST request to the JIRA API with the predefined payload.

A new JIRA story is created automatically.
