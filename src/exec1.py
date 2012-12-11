'''
Created on 05/12/2012

@author: gustavo
'''
from math import sqrt

def resolveEquacao(a,b,c,x=None):
    if x != None:
        y = (a*(x*x)) - (b*x) + c
        return y
    else:
        raiz = (b*b) - (4*a*c)
        x1 = ( -b + sqrt(raiz) ) / ( 2*a )
        x2 = ( -b - sqrt(raiz) ) / ( 2*a )
        return [x1,x2]


print resolveEquacao(1,-5,6)
