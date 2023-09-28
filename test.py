import requests

payload = {
    "message":"Hello from SANDBOX",
    "recepients":['+254743413621']
}

resp = requests.post('https://edu-hub-sms-service-1.vercel.app/send',json=payload).json()
print(resp)