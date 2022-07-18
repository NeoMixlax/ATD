import Client
import ExcelInteract

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

def newValueCoin(coinsAmount: int, moneda):
    price = getPrice(moneda)
    ExcelInteract.modifyCellValue(coinsAmount+2, 9, "Análisis", moneda)
    if stringToChar(moneda)[len(moneda)-3] == "B" and stringToChar(moneda)[len(moneda)-2] == "T" and stringToChar(moneda)[len(moneda)-1] == "C":
        ExcelInteract.modifyCellValue(coinsAmount+2, 10, "Análisis", float(price), "₿* #,##0.000000")
    else:
        ExcelInteract.modifyCellValue(coinsAmount+2, 10, "Análisis", float(price))

def stringToChar(word: str):
    return [char for char in word]
