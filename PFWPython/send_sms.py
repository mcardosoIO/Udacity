from twilio.rest import TwilioRestClient

account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+",    # Replace with your phone number
    from_="+5519") # Replace with your Twilio number

print(message.sid)


#sms service thru twilio phone is not available to brazil
