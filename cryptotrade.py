apikey = "xxx"
apisecret = "xxx"
TESTING = True

import ccxt

exchange = ccxt.binance({
    'apiKey':apikey,
    'secret':apisecret,
    'options':{
        'defaultType':"future"
    }
})

exchange.set_sandbox_mode(True)

def checkwallet():
    res = exchange.fetch_balance()["info"]["assets"]
    result = ""
    for item in res:
        if item["asset"] == "USDT" or item["asset"] == "BUSD":
            result += "Your amount of " + item["asset"] + " is " + str(item["walletBalance"])
            result += "\n"
    
    return result



"""
1. openLong
2. closeLong
3. openShort
4. closeShort
"""

def openlong(pair,amount):
    r = exchange.create_order(
        symbol=pair,
        type="market",
        side="buy",
        amount=amount,
        params={
            "positionSide":"LONG"
        }
    )
    
    return r

def closelong(pair,amount): 
    """short คืน ในฝั่ง long"""
    r = exchange.create_order(
        symbol=pair,
        type="market",
        side="sell",
        amount=amount,
        params={
            "positionSide":"LONG"
        }
    )
    
    return r

def openshort(pair,amount):
    r = exchange.create_order(
        symbol=pair,
        type="market",
        side="sell",
        amount=amount,
        params={
            "positionSide":"SHORT"
        }
    )
    
    return r

def closeshort(pair,amount): 
    """short คืน ในฝั่ง long"""
    r = exchange.create_order(
        symbol=pair,
        type="market",
        side="buy",
        amount=amount,
        params={
            "positionSide":"SHORT"
        }
    )
    
    return r

"""print(checkwallet())"""
