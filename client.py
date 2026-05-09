import os
import requests

a = os.getenv("A", 1)
b = os.getenv("B", 2)

url = f"http://sum-service:5000/sum?a={a}&b={b}"

response = requests.get(url)
print("Response:", response.json()) 