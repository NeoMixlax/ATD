import Credenciales
from binance.client import Client

cliente = Client(Credenciales.api_key, Credenciales.secret_key)
symbols = cliente.get_all_tickers()
