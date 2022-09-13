from helperFunction import *
from cli import *
from Num import *
from Sym import *
from Data import *

updateCli()
eg = {}
args = getArguments()

def runs(test):
    out = False
    if test in eg:
        if(args["dump"]):
            out = eg[test]()
        else:
            try:
                out = eg[test]()
                if(out):
                    print("!!!!!! ", "PASS   ", test, "    true")
                else:
                    print("!!!!!! ", "PASS   ", test, "    false")
            except:
                print("!!!!!! ", "CRASH   ", test, "    false")

def BAD():
    print(eg.this_is_not_there)
    
def LIST():
    print("Examples lua csv -e ...")
    for key in eg:
        print("\t" + key)
    return True

def the():
    printDic(args)
    return True

def sym():
    sym = Sym()
    list = ["a","a","a","a","b","b","c"]
    for x in list:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    printDic({"mid": mode,"div": entropy})
    return True

def num():
    num = Num(0, "num")
    for i in range(1,101):
        num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid , "    ", div)
    return True 

def bignum():
    num = Num(0, "num")
    oldNums = args["nums"]
    updateValue("nums", 32)
    for i in range(1,1000):
        num.add(i)
    printArr(num.nums())
    retVal = len(num._has) == args["nums"]
    updateValue("nums", oldNums)
    return retVal

def csv():
    Lines = readCSV(args["file"])
    for i in range(0,10):
        printArr(Lines[i].split(args["Seperator"]))
    return True

def data():
    data = Data(args["file"])
    for num in data.nums:
        if(num != 0):
            new = vars(num).copy()
            del new['_has']
            printDic(new)
    return True

def stats():
    data = Data(args["file"])
    xmid = {}
    xdiv = {}
    ymid = {}
    ydiv = {}
    for sym in data.syms:
        if(sym != 0):
            xmid[sym.name] = sym.mid()
            xdiv[sym.name] = sym.div()
    for num in data.nums:
        if(num != 0):
            ymid[num.name] = num.mid()
            ydiv[num.name] = num.div()
    print("xmid", end="   ") 
    printDic(xmid)
    print("xdiv", end="   ") 
    printDic(xdiv)
    print("ymid", end="   ") 
    printDic(ymid)
    print("ydiv", end="   ") 
    printDic(ydiv)
    return True

def ALL():
    for test in eg:
        if(test != "ALL"):
            print("\n-----------------------------------")
            runs(test)

eg = {
    "BAD": BAD,
    "LIST": LIST,
    "the": the,
    "sym": sym,
    "num": num,
    "bignum": bignum,
    "csv": csv,
    "data": data,
    "stats": stats,
    "ALL": ALL
}

runs(args["eg"])