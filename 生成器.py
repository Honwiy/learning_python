# -*- coding: utf-8 -*-

print('-----生成器-----')
g = (x * x for x in range (10))
for n in g:
    print(n)

#斐波那契数列
print('-----斐波那契数列算法-----')
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1

fib(5)

#杨辉三角
print('-----杨辉三角生成器-----')
def triangels():
    L=[1]
    while True:
        yield L
        L=[L[x]+L[x+1] for x in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
        

n = 0
for t in triangels():
    print(t)
    n = n + 1 
    if n == 10:
        break