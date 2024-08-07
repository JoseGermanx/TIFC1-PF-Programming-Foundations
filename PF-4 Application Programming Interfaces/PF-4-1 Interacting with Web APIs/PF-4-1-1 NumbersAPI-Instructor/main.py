import json
import requests

response = requests.get("http://numbersapi.com/42?json")

trivia = json.loads(response.content)

print(trivia)
