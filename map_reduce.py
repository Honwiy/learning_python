# -*- coding: utf-8 -*-
#map
def normalize(name):
    name = name.capitalize()
    print(name)

L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))

#reduce
from functools import reduce
def prod(L):
    return reduce(lambda x, y : x*y, L)
print("3*5*7*9 =",prod([3,5,7,9]))

#map_reduce->str2float
def str2float(x):
    def fn(a,b):
        return a*10+b
    n=x.index('.')
    s1=list(map(int,[x for x in x[:n]]))
    s2=list(map(int,[x for x in x[n+1:]]))
    return reduce(fn,s1) + reduce(fn,s2)/10**len(s2)
print('123.456 =',str2float('123.456'))