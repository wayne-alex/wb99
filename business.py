from twilio.rest import Client

def sendMessage(body,to):
  account_sid = 'AC5903aa13a63852688799a727440dc6d2'
  auth_token = '265d556b39b4e80765dd80ec483da356'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=body,
    to='whatsapp:'+to
  )

  print(message.sid)


