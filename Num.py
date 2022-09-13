import imp
import sys
import math
from helperFunction import *
import re
from cli import *
import random

class Num:
    def __init__(self, c=0, s=""):
        str = re.search('([0-9a-zA-Z:\+-]+)[/n]?', s).group(1)
        self.n = 0
        self.at = c
        self.name = str
        self._has = []
        self.lo = sys.float_info.max
        self.hi = -sys.float_info.min
        self.isSorted = True
        self.w = -1 if re.search("-$", str) else 1

    def nums(self):
        if not self.isSorted:
            self._has.sort()
            self.isSorted = True
        return self._has

    def add(self, v):
        if v != "?":
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            nums = getArguments()["nums"]
            if len(self._has) < nums:
                self._has.append(v)
            elif random.random() < nums/self.n:
                pos = random.randint(0, len(self._has)-1)
                self._has[pos] = v
            self.isSorted = False

    def div(self):
        a = self.nums(); 
        return rnd((per(a,0.9)-per(a,0.1))/2.58, 2)

    def mid(self):
        a = self.nums(); 
        return rnd(per(a, 0.5),2)