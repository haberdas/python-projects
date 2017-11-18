import json

#read a config file and return coins and keys
def readConfig(fileName):
    data = json.load(open(fileName))
    coins = [x["name"] for x in data["coins"]]
    exchanges = [{"name":x["name"],"id":x["id"]} for x in data["exchanges"]]

    res = {"coins":coins, "exchanges":exchanges}

    #returns a dict of all info
    return res
