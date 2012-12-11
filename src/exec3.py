'''
Created on 03/12/2012

@author: gustavo
'''
import re
    
def isNumeroReal(string):
    m = re.compile(r"\d*\,\d\d$")
    if re.match(m,string):
        print 'eh numero real'
    else:
        print 'nao eh numero real'

isNumeroReal('2362,25')
    

    