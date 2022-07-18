""" 
╔═════════════════════════════════════════════════════════╗
║----------------Automated Trading Daily------------------║
║---AUTHOR: Nicolás Andrés Ramírez Calderón (NeoMixlax)---║
║-----DESCR: Display your trades in an Excel workbook-----║
╚═════════════════════════════════════════════════════════╝

Note: NEVER code when you're tired
""" 

import time
import Client
import Monedas
import ExcelInteract
import CompraVenta
import SortTrades
import MatrixToWb
from datetime import datetime
linea = 3 #This is the row's value where you want your table starts placing the data

coinsAmount = 0
tradesMatrix = []
# Modify the bounds of the table for being able to modify the cells's values

ExcelInteract.modifyTable(["I","2"], ["J","2"], "Análisis", "t_Precios")

# Starts looking for the transactions

for moneda in Monedas.getMonedas():
    trades = Client.cliente.get_my_trades(symbol=moneda)
    if len(trades) == 0:
        # I placed a time.sleep() for avoiding to get the too many API request error
        
        time.sleep(0.3)
        continue
    else:
        for transaccion in trades:
            # Getting the transaction's values
            
            columna = 2
            simbolo = transaccion['symbol']
            timeT = transaccion['time']
            fecha = datetime.fromtimestamp(timeT / 1000)
            compra_venta = CompraVenta.getCompra_venta(transaccion['isBuyer'])
            precio = float(transaccion['price'])
            can_obtenida = float(transaccion['qty'])
            can_gastada = float(transaccion['quoteQty'])
            sim_comision = transaccion['commissionAsset']
            comision = float(transaccion['commission'])
            id_ = transaccion['id']

            # Now we're gonna sort the info in a list 
            currentTransaction = [simbolo, fecha, compra_venta, precio, can_obtenida, can_gastada, sim_comision, comision, id_]
            # And append it to our matrix
            tradesMatrix.append(currentTransaction)

        coinsAmount += 1
        
        # Get the coin's value 
        Monedas.newValueCoin(coinsAmount, moneda)       
        
# Now we sort our trades matrix
SortTrades.sort(tradesMatrix)

# We modify the table range to be able to modify it
ExcelInteract.modifyTable(["B","2"], ["J","{}".format(str(linea-1))], "Órdenes", "t_Ordenes")

# And place them in our wb
MatrixToWb.placeMatrix(tradesMatrix)

ExcelInteract.modifyTable(["B","2"], ["J","{}".format(str(len(tradesMatrix)))], "Órdenes", "t_Ordenes")
ExcelInteract.modifyTable(["I","2"], ["J","{}".format(str(coinsAmount+2))], "Análisis", "t_Precios")

ExcelInteract.saveWb()