import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

class AlertManager:
    def __init__(self):
        self.twilio_sid = 'sid'
        self.twilio_token = 'token'
        self.twilio_number = 'twilio number'
        self.recipient_number = 'your verified number'
        self.client = Client(self.twilio_sid, self.twilio_token)

    def send_sms_alert(self, message):
        """
        Sends an SMS alert via Twilio.
        :param message: The message content.
        """
        try:
            print(f"Sending SMS Alert: {message}")  # Debug message before sending
            print(f"From: {self.twilio_number} To: {self.recipient_number}")  # Debug: Check phone numbers

            message = self.client.messages.create(
                body=message,
                from_=self.twilio_number,
                to=self.recipient_number
            )
            print(f"SMS Alert sent: {message.sid}")  # Debug: Success message
        except Exception as e:
            print(f"Failed to send SMS alert: {e}")  # Debug: Error message
