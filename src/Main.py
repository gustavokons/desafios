'''
Created on Dec 9, 2012

@author: gustavokons
'''
from Pessoa import Pessoa

def main():
    p = Pessoa('Gustavo','gustavokons@hotmail.com','32434075')
    #p.inserirRegistroDocs()
    #p.contaLetras()
    p.gerarVCard()

if __name__ == '__main__':
    main()
    
    
