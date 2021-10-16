import requests

text = "test"

r = requests.post('http://localhost:8000/api',data=text.encode(), headers={'Content-Type': 'text/plain'})
print('status:', r.status_code)
print('json:', r.json())