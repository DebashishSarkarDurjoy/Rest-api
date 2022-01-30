import requests
import json

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

response = response.json()

for value in response['items']:
    if value['answer_count'] == 0:
        print(value['title'])
        print(value['link'])
    else:
        print("skipped")

    print()
