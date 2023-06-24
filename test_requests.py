import requests

url = 'http://127.0.0.1:5000/crypto'

# example signal

sig1 = {'action': 'OPEN LONG','pair':'BTCUSDT','amount':0.1} 
sig2 = {'action': 'TPSL LONG 100','pair':'BTCUSDT','amount':0.1}
sig3 = {'action': 'OPEN SHORT','pair':'BTCUSDT','amount':0.1} 
sig4 = {'action': 'TPSL SHORT 100','pair':'BTCUSDT','amount':0.1}



x = requests.post(url, json = sig1)
x = requests.post(url, json = sig3)
print(x.text)