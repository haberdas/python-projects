import requests
import json
import time
import operator

#  Settings
apiUrl = "https://api.coinmarketcap.com/v1/ticker/?limit="
coinLimit = 200
maxSupply = 50000000000

def getPoloCoins():
	r = requests.get('https://poloniex.com/public?command=returnTicker')
	res = r.json()

	#generate a key list of coins
	coinList = [x for x in res if "BTC_" in x]

	#make a usable dictionary from Polo's shit
	coinDict = [{"name":i,"percentChange":res[i]["percentChange"], "last":res[i]["last"], "low24hr":res[i]["low24hr"], "baseVolume":res[i]["baseVolume"]} for i in coinList]
	coinDict.sort(key=operator.itemgetter('name'))

	return coinDict


def filterByVolume(data, limit):
	filteredList = [x for x in data if float(x['baseVolume']) > limit]
	return filteredList

def filterByChange(data, limit):
	filteredList = [x for x in data if float(x['percentChange'])*100 < limit and float(x['percentChange'])*100 > -1 * limit]
	return filteredList

x = getPoloCoins()
y = filterByVolume(x, 50)
z = filterByChange(y, 5)
print z
