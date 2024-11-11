import os
import pickle
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
import sys

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Authenticate and create the Gmail API service
def get_gmail_service(file_pickle):
    creds = None
    if os.path.exists(file_pickle):
        with open(file_pickle, 'rb') as token:
            creds = pickle.load(token)
    else:
        sys.exit(1)
    if not creds or not creds.valid:
        # if creds and creds.expired and creds.refresh_token:
        #     creds.refresh(Request())
        # else:
        #     flow = InstalledAppFlow.from_client_secrets_file(
        #         r"C:\Users\A490629\OneDrive - Volvo Group\Onedrive_Volvo\personal\client_secret.json", SCOPES)
        #     creds = flow.run_local_server(port=0)
        # with open('token.pickle', 'wb') as token:
        #     pickle.dump(creds, token)
        raise Exception("Terminating program because of creds")
    return build('gmail', 'v1', credentials=creds)

# Function to send an email
def send_email(service, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject

    # Encode message and send using the Gmail API
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    try:
        message = (service.users().messages().send(userId="me", body={'raw': raw_message})
                   .execute())
        print(f'Message sent successfully. Message Id: {message["id"]}')
    except Exception as e:
        print(f"An error occurred: {e}")

