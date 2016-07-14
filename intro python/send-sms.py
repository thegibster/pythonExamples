from twilio.rest import TwilioRestClient

account_sid = "ACe4855de3dddb311fe9ce5951ce99be4e" # Your Account SID from www.twilio.com/console
auth_token  = "8a20ac60bcd0d3b9de81fbc79d423431"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+13233134979",    # Replace with your phone number
    from_="+14246660400") # Replace with your Twilio number

print(message.sid)
