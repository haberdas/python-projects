
from apis import poloniex, bittrex, gdax
import utils

#read config file
configInfo = utils.readConfig("config.json")
#initialize APIs
exchanges = [{"api":poloniex}, {"api":bittrex}, {"api":gdax}]

#call public "all coin ticker" APIs
def publicApis(exchanges):

    res = []
    for i in exchanges:
        try:
            res.append(i["api"].getAllCoins())
        except AttributeError:
            print "Error: No getAllCoins for "+ str(i["api"])
    #print res

    return res

print publicApis(exchanges)
