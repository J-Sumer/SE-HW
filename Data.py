from Sym import *
from Num import *
from helperFunction import *
import re

class Data:
    def __init__(self, file=""):
        self.syms = []
        self.nums = []
        csv(self, file)

def csv(data, file):
    Lines = readCSV(file)
    firstLine = Lines[0].split(',')
    for idx, col in enumerate(firstLine):
        if re.search("[-+!]", col):
            data.nums.append(Num(idx+1,col))
            data.syms.append(0)
        elif re.search("[:]$", col):
            data.nums.append(0)
            data.syms.append(0)
        else:
            data.nums.append(0)
            data.syms.append(Sym(idx+1,col))

    for i in range(1,len(Lines)):
        currLine = Lines[i].split(',')
        for idx, num in enumerate(currLine):
            if(data.syms[idx] != 0):
                data.syms[idx].add(getNumber(num))
            elif(data.nums[idx] !=0):
                data.nums[idx].add(getNumber(num))
    return Lines

# data = Data('./csv/test.csv')
# print(data.syms[0].mid())