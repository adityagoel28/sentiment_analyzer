import requests

query = {'text': 'आप एक अच्छे इंसान हैं'}
response = requests.get(
    'http://127.0.0.1:8000/sentiment_analysis/', params=query)
print(response.json())