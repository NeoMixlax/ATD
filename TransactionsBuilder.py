import time
import Transaccion
import Coin
import Wallet
import OptimizerTransactionsBuilder
from datetime import datetime

myWallet = Wallet.Wallet()
def buildTransactions():
    i=0
    for moneda in OptimizerTransactionsBuilder.getMonedas():
        trades = OptimizerTransactionsBuilder.cliente.get_my_trades(symbol=moneda)
        if len(trades) == 0:
            time.sleep(0.3) # I placed a time.sleep() for avoiding to get the too many API request error
            continue
        else:
            myWallet.agregarMoneda(Coin.Coin(moneda, OptimizerTransactionsBuilder.getPrice(moneda)))
            for transaccion in trades:
                # Getting the transaction's values

                simbolo = transaccion['symbol']
                timeT = transaccion['time']
                fecha = datetime.fromtimestamp(timeT / 1000)
                compra_venta = OptimizerTransactionsBuilder.getCompra_venta(transaccion['isBuyer'])
                precio = float(transaccion['price'])
                can_obtenida = float(transaccion['qty'])
                can_gastada = float(transaccion['quoteQty'])
                sim_comision = transaccion['commissionAsset']
                comision = float(transaccion['commission'])
                id_ = transaccion['id']

                myWallet.monedas[i].agregarTransaccion(Transaccion.Transaccion(simbolo, fecha, compra_venta, precio, can_obtenida, can_gastada, sim_comision, comision, id_))
            i += 1
    myWallet.getTodasTransacciones()