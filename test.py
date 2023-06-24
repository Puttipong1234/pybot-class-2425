# variable : string , integer , float , list , dictionary 

# string

a = "hello"
b = "world"

result = a + b
print(result)

word = "BTCUSDT OPEN LONG"
words = word.split(" ")
print(words[0])

# integer , float , [+ - * /]

c = 1
d = 2.50
e = 0.15

print(c+d+e)

# list 

data = ["btcusd","ethusd","xauusd","eurusd"]

# append 

pair = "bnbusd"

data.append(pair)

print(data)

# for loop

for item in data:
    print("TRADING PAIR : " +  item)
    
# dictionary key , value

data = { "สุนัข" : "dog" , "นก" : "bird" }

print(data["นก"])

# function f(x) = x + 13 , f(1) = 14 , f(2) = 15

def myfunction(x):
    f_x = x + 13
    return f_x

result = myfunction(x=5) # 18
print(result)

def buyBTC(amount):
    btc_price = 30000
    return amount * btc_price

print( "pay amount usd : " + str(buyBTC(2)))
print( "pay amount usd : " + str(buyBTC(10)))

