import africastalking
import os
from dotenv import load_dotenv
load_dotenv()

# TODO: Initialize Africa's Talking

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
            print(f"{message_response['SMSMessageData']['Message']}")

        except Exception as e:
            print(f"Aw snap! It didn't work, here is the error : {e}")


