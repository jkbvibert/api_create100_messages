#CSE-59031
import requests
import json

headers = {'Content-Type': 'application/json;charset=utf-8','li-api-session-key': '<sanitized>.'}

data = {
	"data":{
		"type":"message",
		"body":"This is the message body",
		"topic": {
			"id": 766
		},
		"parent": {
			"id": 766
		}
	}
}

for x in range(103):
	r = requests.post(url = "https://<sanitized>/api/2.0/messages/", data = json.dumps(data, default=str), headers=headers)
	r_formatted = r.json()
print(r_formatted)