import openai
import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZmNhMzE1NzQtZWZkYS00MWM5LWE1MGQtNGRiYmEwYTZkNjMzIiwidHlwZSI6ImFwaV90b2tlbiJ9.FdfHmAFqzsK9NEpodqgztHRw9gPjE0BhgtGhFVsa-l8"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello tell me a joke!...  ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "abcd"
}

#response = requests.post(url, json=payload, headers=headers)

#result = json.loads(response.text)
#print(result['openai']['generated_text'])


def aicall(query):
    payload["text"] = query
    #print(payload)
    response = requests.post(url, json=payload, headers=headers)
    #print(response.text)
    result = json.loads(response.text)
    print(result['openai']['generated_text'])
aicall("how are you...")