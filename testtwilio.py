from twilio.rest import Client

# Add your Twilio credentials directly for testing
account_sid = 'AC0c314ab6dbac09517a0f04ccb48512a1'
auth_token = '555b145aed89918eb6708780efa32e67'
twilio_number = '+12564641084'
recipient_number = '+917302876582'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Test alert from Twilio.",
    from_=twilio_number,
    to=recipient_number
)

print(f"Message sent: {message.sid}")
