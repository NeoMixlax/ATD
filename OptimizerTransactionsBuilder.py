import Credenciales
from binance.client import Client

symbols = Client(Credenciales.api_key, Credenciales.secret_key).get_all_tickers()
cliente = Client(Credenciales.api_key, Credenciales.secret_key)

def getCompra_venta(com_ven: bool):
    if com_ven:
        return 'Compra'
    else:
        return 'Venta'

def getMonedas():
    monedas = []
    for symbol in symbols:
        monedas.append(symbol['symbol'])
    return monedas

def getPrice(coin):
    for symbol in symbols:
        if coin == symbol['symbol']:
            price = float(symbol['price'])
            return price
