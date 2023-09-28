import requests

payload = {
    "message":"Hello from SANDBOX",
    "recepients":['+254743413621']
}

resp = requests.post('http://127.0.0.1:3000/send',json=payload).json()
print(resp)