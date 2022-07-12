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
from datetime import datetime

linea = 3
coinsAmount = 0

# Modify the bounds of the table for being able to modify the cells's values

ExcelInteract.modifyTable(["$B","$2"], ["$K","${}".format(str(linea-1))], "Órdenes", "t_Ordenes")
ExcelInteract.modifyTable(["$I","$2"], ["$J","$2"], "Análisis", "t_Precios")

# Starts looking for the transactions

for moneda in Monedas.getMonedas():
    coinTransactionsAmount=0
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
            fechaHora = datetime.fromtimestamp(timeT / 1000)
            fechaHoraSplited = str(fechaHora).split()
            fecha = fechaHoraSplited[0]
            hora = fechaHoraSplited[1]
            compra_venta = CompraVenta.getCompra_venta(transaccion['isBuyer'])
            precio = float(transaccion['price'])
            can_obtenida = float(transaccion['qty'])
            can_gastada = float(transaccion['quoteQty'])
            sim_comision = transaccion['commissionAsset']
            comision = float(transaccion['commission'])
            id_ = transaccion['id']
            
            # Simbolo
            ExcelInteract.modifyCellValue(linea, columna, simbolo, "Órdenes")

            # fecha
            ExcelInteract.modifyCellValueDate(linea, columna + 1, fecha, "Órdenes")

            # Hora
            ExcelInteract.modifyCellValueHour(linea, columna + 2, hora, "Órdenes")

            # Compra/Venta
            ExcelInteract.modifyCellValue(linea, columna + 3, compra_venta, "Órdenes")

            # Precio 
            ExcelInteract.modifyCellValue(linea, columna + 4, precio, "Órdenes")

            # Cantidad obtenida
            ExcelInteract.modifyCellValue(linea, columna + 5, can_obtenida, "Órdenes")

            # Cantidad gastada
            ExcelInteract.modifyCellValue(linea, columna + 6, can_gastada, "Órdenes")

            # Simbolo de comisión 
            ExcelInteract.modifyCellValue(linea, columna + 7, sim_comision, "Órdenes")

            # Comisión valor 
            ExcelInteract.modifyCellValue(linea, columna + 8, comision, "Órdenes")

            # Id
            ExcelInteract.modifyCellValue(linea, columna + 9, id_, "Órdenes")

            linea += 1
            if coinTransactionsAmount==0:
                # Update the coins amount

                coinsAmount = coinsAmount+1
                # Get the coin's value
                
                price = Monedas.getPrice(moneda)
                ExcelInteract.modifyCellValue(coinsAmount+2, 9, moneda, "Análisis")
                ExcelInteract.modifyCellValue(coinsAmount+2, 10, float(price), "Análisis")
            coinTransactionsAmount=coinTransactionsAmount+1
        
        ExcelInteract.modifyTable(["$I","$2"], ["$J","${}".format(str(coinsAmount+2))], "Análisis", "t_Precios")
        ExcelInteract.modifyTable(["$B","$2"], ["$K","${}".format(str(linea-1))], "Órdenes", "t_Ordenes")
        ExcelInteract.saveWb()
