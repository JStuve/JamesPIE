# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import config
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from Brain import getTask

account_sid = config.account_sid
auth_token  = config.auth_token

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/sms', methods=['POST'])

def sms():
    message = request.values.get('Body', None)
    resp = MessagingResponse()
    resp.message(getTask(message))
    return str(resp)

def sendSMS(msg):
    message = client.messages.create(
        to= config.Master_number, 
        from_= config.James_number,
        body= msg
        )



if __name__ == "__main__":
    ### Test
#    WoLTest = "James Can you turn on my computer!"
#    crateTest = "Hey, open up stellas crate"
#    powerOff = "James, power down everything"
#    
#    msg = getTask(WoLTest)
#    print("Brain shall perform: " + msg)

    #Official
    app.run(debug=True)


