from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    sender = str(request.form.get('Sender'))

    # Create reply
    resp = MessagingResponse()
    resp.message("Hello there "+sender+",\n Welcome to Family First Bank\n How can i help you today?")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

