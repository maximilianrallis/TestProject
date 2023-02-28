import os
import base64
import email
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Set up authentication
creds, project_id = google.auth.default(scopes=['https://www.googleapis.com/auth/gmail.readonly'])
if not isinstance(creds, Credentials):
    raise ValueError('Invalid credentials')

# Create the Gmail API client
gmail = build('gmail', 'v1', credentials=creds)

# Call the API to retrieve the list of messages in your inbox
response = gmail.users().messages().list(
    userId='me',
    labelIds=['INBOX']
).execute()

# Print the list of message IDs
if 'messages' in response:
    messages = response['messages']
    for message in messages:
        msg = gmail.users().messages().get(userId='me', id=message['id']).execute()
        payload = msg['payload']
        headers = payload['headers']
        for header in headers:
            if header['name'] == 'From':
                print(header['value'])
            if header['name'] == 'Subject':
                print(header['value'])
            if header['name'] == 'Date':
                print(header['value'])
        print('--------------------------------------')
else:
    print('No messages found.')
