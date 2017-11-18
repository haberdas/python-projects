import requests
import operator

# public API calls
#
#get ticker for all coins on Polo relative to BTC
#returns a dictionary in form {"name":"","last":""...} see docs
def getAllCoins():
    poloCall = "https://poloniex.com/public?command=returnTicker"

    #call the polo api
    r = requests.get(poloCall)
    res = r.json()

    #generate a key list of coins
    coinList = [x for x in res if "BTC_" in x]

    #make a usable dictionary from Polo's shit
    coinDict = [{"name":i,"percentChange":res[i]["percentChange"], "last":res[i]["last"],
            "low24hr":res[i]["low24hr"], "baseVolume":res[i]["baseVolume"]} for i in coinList]
    coinDict.sort(key=operator.itemgetter('name'))
    resDict = {"name":"poloniex","data":coinDict}

    return resDict
