from twilio.rest import Client

# Add your Twilio credentials directly for testing
account_sid = 'SID'
auth_token = 'token'
twilio_number = 'twilio number'
recipient_number = 'number'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Test alert from Twilio.",
    from_=twilio_number,
    to=recipient_number
)

print(f"Message sent: {message.sid}")
