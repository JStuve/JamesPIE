# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import config
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

account_sid = config.account_sid
auth_token  = config.auth_token

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/sms', methods=['POST'])

def sms():
    message = request.form['Body']
    
    resp = twiml.Response()
    resp.message('Hello, Josh!')
    
    return str(resp)

def sendSMS():
    message = client.messages.create(
        to= config.Master_number, 
        from_= config.James_number,
        body="Hello from Python!"
        )


if __name__ == "__main__":
    app.run(debug=True)


