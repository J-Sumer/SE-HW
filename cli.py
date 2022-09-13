import random
import sys

arguments = {
    "eg": "nothing",
    "dump": False,
    "file": "./csv/test.csv",
    "help": False,
    "nums": 512,
    "seed": 10019,
    "Seperator": ","
}

def updateCli():
    for idx, arg in enumerate(sys.argv):
        for key, value in arguments.items():
            if((arg == "--" + key) or (arg == "-" + key[0:1])):
                arguments[key] = coerce(sys.argv[idx+1])
    random.seed(arguments["seed"])

def updateValue(key, val):
    arguments[key] = val

def coerce(str):
    if(str.lower() == "true"):
        return True
    if(str.lower() == "false"):
        return False
    try:
        return int(str)
    except:
        pass
    return str.strip()

def getArguments():
    return arguments