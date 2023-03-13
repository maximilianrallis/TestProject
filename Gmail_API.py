import os
import google.auth
from googleapiclient.discovery import build

creds_path = r"C:\Users\WF6444\PycharmProjects\TestProject\client_secret.json"

# Get credentials and create Gmail API client
creds, project_id = google.auth.default(scopes=["https://www.googleapis.com/auth/gmail.readonly"])
service = build("gmail", "v1", credentials=creds)

# Get the email addresses of the last 5 messages in the inbox
results = service.users().messages().list(userId='me', maxResults=5).execute()
messages = results.get("messages", [])

for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    headers = msg['payload']['headers']
    for header in headers:
        if header['name'] == 'From':
            print(header['value'])

