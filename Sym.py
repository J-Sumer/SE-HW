import math
from helperFunction import *

class Sym:
    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}

    def add(self, v):
        if v != '?':
            self.n += 1
            if v in self._has:
                self._has[v] = 1 + self._has[v]
            else:
                self._has[v] = 1
                
    def mid(self):
        most = -1
        mode = None
        for key, value in self._has.items():
            if value > most:
                most = value
                mode = key
        return mode

    def fun(self, p):
        return p*math.log(p,2)

    def div(self):
        e = 0
        for k,n in self._has.items():
            if n>0:
                e = e - self.fun(n/self.n)
        return rnd(e,2)


