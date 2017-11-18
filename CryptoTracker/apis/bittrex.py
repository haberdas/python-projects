import requests
import operator

# public API calls
#
#get ticker for all coins on Polo relative to BTC
#returns a dictionary in form {"name":"","last":""...} see docs
def getAllCoins():
    bitCall = "https://bittrex.com/api/v1.1/public/getmarketsummaries"

    #call the bittrex api
    r = requests.get(bitCall)
    res = r.json()

    #Volume comes back in a weird format, need to figure that out
    coinDict = [{"name":i["MarketName"].replace("-","_"),"baseVolume":i["Volume"],
                "last":i["Last"], "low24hr":i["Low"],
                "percentChange":(i['PrevDay']-i["Last"])/i['PrevDay']*100
                } for i in res["result"] if "BTC" in i["MarketName"] ]

    resDict = {"name":"bittrex","data":coinDict}

    return resDict
