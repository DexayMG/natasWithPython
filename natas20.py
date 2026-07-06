import requests

url="http://natas20.natas.labs.overthewire.org"
auth=("natas20","p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw")

data = {"username": "admin"}
response1 = requests.post(url, auth=auth, data=data)
response2 = requests.get("http://natas20.natas.labs.overthewire.org/index.php?debug", auth=auth)
print(response2.text)