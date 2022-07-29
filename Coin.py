import SortTrades
import Transaccion

class Coin:

    def __init__(self, simbolo, precio):
        self.simbolo = simbolo
        self.precio = precio
        self.transacciones = []
        self.transaccionesCompra = []
        self.transaccionesVenta = []
        self.canTransacciones = 0
        self.canTcom = 0
        self.canTven = 0

    def agregarTransaccion(self, Transaccion: Transaccion):
        self.transacciones.append(Transaccion)
        self.canTransacciones += 1
        if Transaccion.compraVenta == 'Compra':
            self.transaccionesCompra.append(Transaccion)
            self.canTcom += 1
        else:
            self.transaccionesVenta.append(Transaccion)
            self.canTven += 1
        self.ordenarTransacciones()

    def getCantidadMoneda(self):
        total = 0
        for transaccion in self.transaccionesCompra:
            total += transaccion.canObtenida
        for transaccion in self.transaccionesVenta:
            total = total-transaccion.canGastada
        return total

    def getRelacionBtc(self):
        total = 0
        for transaccion in self.transaccionesCompra:
            total = total - transaccion.canGastada 
        for transaccion in self.transaccionesVenta:
            total += transaccion.canObtenida

    def ordenarTransacciones(self):
        SortTrades.ordenarTransacciones([self.transacciones, self.transaccionesCompra, self.transaccionesVenta])