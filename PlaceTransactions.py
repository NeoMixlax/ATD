import TransactionsBuilder
import ExcelInteract

format1 = """"USDT"* #,##0.000000"""
format2 = """[$₿-x-xbt2] #,##0.000000"""
allTran =  TransactionsBuilder.myWallet.transaccionesTotales
def placeOrdenes():
    ExcelInteract.modifyTable(["B","2"], ["J","2"], "Órdenes", "t_Ordenes")
    for i in range(len(allTran)):
        ExcelInteract.modifyCellValue(i+3, 2, "Órdenes", allTran[i].simbolo)
        ExcelInteract.modifyCellValue(i+3, 3, "Órdenes", allTran[i].fecha, "d/mm/yyyy")
        ExcelInteract.modifyCellValue(i+3, 4, "Órdenes", allTran[i].compraVenta)
        ExcelInteract.modifyCellValue(i+3, 5, "Órdenes", allTran[i].precio, format2)
        ExcelInteract.modifyCellValue(i+3, 6, "Órdenes", allTran[i].canObtenida)
        ExcelInteract.modifyCellValue(i+3, 7, "Órdenes", allTran[i].canGastada, format2)
        if allTran[i].simbolo == 'BTCUSDT':
            ExcelInteract.modifyCellValue(i+3, 5, "Órdenes", allTran[i].precio, format1)
            ExcelInteract.modifyCellValue(i+3, 7, "Órdenes", allTran[i].canGastada, format1)
            ExcelInteract.modifyCellValue(i+3, 6, "Órdenes", allTran[i].canObtenida, format2)
        ExcelInteract.modifyCellValue(i+3, 8, "Órdenes", allTran[i].simComision)
        ExcelInteract.modifyCellValue(i+3, 9, "Órdenes", allTran[i].comision)
        ExcelInteract.modifyCellValue(i+3, 10, "Órdenes", allTran[i].iD)
    ExcelInteract.modifyTable(["B","2"], ["J",i+3], "Órdenes", "t_Ordenes")
    ExcelInteract.saveWb()

allCoins = TransactionsBuilder.myWallet.monedas
def placeValues():
    ExcelInteract.modifyTable(["I","2"], ["L","2"], "Análisis", "t_Precios")
    for i in range(len(allCoins)):
        ExcelInteract.modifyCellValue(i+3, 9, "Análisis", allCoins[i].simbolo)
        ExcelInteract.modifyCellValue(i+3, 10, "Análisis", allCoins[i].precio, format2)
        ExcelInteract.modifyCellValue(i+3, 11, "Análisis", allCoins[i].getCantidadMoneda())
        ExcelInteract.modifyCellValue(i+3, 12, "Análisis", allCoins[i].getCantidadMoneda()*allCoins[i].precio)
        if allCoins[i].simbolo == 'BTCUSDT':
            ExcelInteract.modifyCellValue(i+3, 10, "Análisis", allCoins[i].precio, format1)
            ExcelInteract.modifyCellValue(i+3, 11, "Análisis", allCoins[i].getCantidadMoneda(), format2)
            ExcelInteract.modifyCellValue(i+3, 12, "Análisis", allCoins[i].getCantidadMoneda()*allCoins[i].precio, format1)
    ExcelInteract.modifyTable(["I","2"], ["L",i+3], "Análisis", "t_Precios")
    ExcelInteract.saveWb()

def placeAll():
    placeOrdenes()
    placeValues()
