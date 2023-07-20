import requests
import json

host = 'localhost'
port = 5000
url = "http://localhost:5000/"

x = requests.get(url)
print(x)
print(x.text)

data = {"Review": 'This movie is great.'}
data = json.dumps(data)
print(data)

url = "http://localhost:5000/get_sentiment"
x = requests.post(url, data)
print(x)
print(x.text)

#Making compact API
url = "http://localhost:5000/get_sentiment"
data = {"Review": 'This movie is worst. Return my money'}
data = json.dumps(data)

x = requests.post(url, data)
print(json.loads(x.text)['result'])