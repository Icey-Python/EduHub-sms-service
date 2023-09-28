import os
from flask import Flask, request
from flask_cors import cross_origin,CORS
import africastalking
import os
from dotenv import load_dotenv
load_dotenv()

# TODO: Initialize Africa's Talking

app = Flask(__name__)
CORS(app)
username = os.environ.get('username')
api_key= os.environ.get('api_key')
africastalking.initialize(username,api_key)

class send_sms():
    sms = africastalking.SMS       
    def send(self,recepients:list,message:str,sender:str):
        print('sending message')
        #TODO: Send message
        receivers:list = recepients
        message_body :str = message
        sender = sender
        
        try:
            message_response = self.sms.send(message_body,receivers,sender)

            #log the status and response of the message sent
            return {"message":f"(Message sent) {message_response['SMSMessageData']['Message']}"}

        except Exception as e:
            return {"Error":f"Aw snap! It didn't work, here is the error : {e}"}




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

if __name__ == "__main__":
    #TODO: Call send message function 
    app.run(debug=True, port =3000)
