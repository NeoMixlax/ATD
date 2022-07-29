import SortTrades
import Transaccion
import Coin

class Wallet:
    def __init__(self):
        self.monedas = []
        self.transaccionesTotales = []
        self.transaccionesTotalesCompra = []
        self.transaccionesTotalesVenta = []
        self.canMonedas = 0

    def agregarMoneda(self, moneda: Coin):
        self.monedas.append(moneda)
        self.canMonedas += 1

    def agregarTransaccion(self, transaccion: Transaccion):
        for moneda in self.monedas:
            if moneda.simbolo == transaccion.simbolo:
                moneda.agregarTransaccion(transaccion)
                break

    def getTodasTransacciones(self):
        self.getTransaccionesTotales()
        self.getTransaccionesCompra()
        self.getTransaccionesVenta()
        self.ordenarTodasTransacciones()

    def getTransaccionesTotales(self):
        self.transaccionesTotales.clear()
        for moneda in self.monedas:
            for transaccion in moneda.transacciones:
                self.transaccionesTotales.append(transaccion)

    def getTransaccionesCompra(self):
        self.transaccionesTotalesCompra.clear()
        for moneda in self.monedas:
            for transaccion in moneda.transaccionesCompra:
                self.transaccionesTotalesCompra.append(transaccion)

    def getTransaccionesVenta(self):
        self.transaccionesTotalesVenta.clear()
        for moneda in self.monedas:
            for transaccion in (moneda.transaccionesVenta):
                self.transaccionesTotalesVenta.append(transaccion)

    def getBtc(self):
        total = 0
        for moneda in self.monedas:
            if moneda.simbolo == 'BTCUSDT':
                total += moneda.getCantidadMoneda()
            else:
                total += moneda.getRelacionBtc()
        return total

    def ordenarTodasTransacciones(self):
        SortTrades.ordenarTransacciones([self.transaccionesTotales, self.transaccionesTotalesCompra, self.transaccionesTotalesVenta])
