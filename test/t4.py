import requests
import json


payload = """{
    "msg": ["静夜思"],
    "b": 1
}"""

headers = {"Content-Type": "application/json; charset=UTF-8"}

# result = requests.post("https://api.apiopen.top/getJoke", data=json.dumps(payload), verify=False)
# result = requests.get("https://api.apiopen.top/getJoke?page=1&count=2&type=video", verify=False)
result = requests.get("http://api.wpbom.com/api/ancien.php?msg=[静夜思]&b=1")
# result = requests.post("http://api.wpbom.com/api/ancien.php", data=payload, headers=headers)
#
#
print(result.text)