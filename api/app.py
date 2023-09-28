import os
from flask import Flask, request
from flask_cors import cross_origin,CORS
from at_sms import send_sms

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "This is the index route: use `/send` to send messages"

#send message to recepient
@cross_origin()
@app.route("/send", methods=['POST'])
def send():
    data = request.get_json()
    recepients:str = data['recepients']
    message:list = data['message']
    sender_id:str = "15021"

    send_sms().send(recepients=recepients,message=message,sender=sender_id)
    return {"message":"Sent"}

if __name__ == "__main__":
    #TODO: Call send message function 
    app.run(debug=True, port =3000)
