import math
import re

def per(arr, position):
    position = math.floor(((position) * len(arr)) + 0.5)
    return arr[max(1, min(len(arr), position))-1]

def push(arr, ele):
    arr.append(ele)
    return ele

def rnd(num, places):
    mult = 10^(places or 2)
    return (math.floor(num * mult + 0.5)) / mult

def getNumber(s):
    num = s.strip()
    m = re.search('([0-9]+.[0-9]*)/n', s)
    if m:
        num = m.group(1)
    return float(num)

def getTrimmedString(s):
    return re.search('([0-9a-zA-Z:\+-]+[.]?[0-9]*)[/n]?', str(s)).group(1)

def printDic(dic):
    string = "{"
    for key, value in dic.items():
        string = string + ":" + key + " " + str(value) + " "
    string += "}"
    print(string)

def printArr(arr):
    string = "{"
    for val in arr:
        string += getTrimmedString(val) + " "
    string = string + "}"
    print(string)

def readCSV(file):
    fileContent = open(file, 'r')
    Lines = fileContent.readlines()
    return Lines