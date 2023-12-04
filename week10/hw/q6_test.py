from time import sleep
import requests

url = "http://localhost:9696/predict"
client = {"job": "retired", "duration": 445, "poutcome": "success"}

for i in range(10):  
    sleep(1)
    response = requests.post(url, json=client).json()
    print(response)

