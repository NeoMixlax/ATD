from symtable import Symbol
import Client

def getMonedas():
    monedas = []
    for symbol in Client.symbols:
        monedas.append(symbol['symbol'])
    return monedas

def getPrice(coin):
    for symbol in Client.symbols:
        if coin == symbol['symbol']:
            price = symbol['price']
            return price