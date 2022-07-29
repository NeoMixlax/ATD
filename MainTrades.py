""" 
╔═════════════════════════════════════════════════════════╗
║----------------Automated Trading Daily------------------║
║---AUTHOR: Nicolás Andrés Ramírez Calderón (NeoMixlax)---║
║-----DESCR: Display your trades in an Excel workbook-----║
╚═════════════════════════════════════════════════════════╝

Note: NEVER code when you're tired
""" 

import PlaceTransactions
import TransactionsBuilder

TransactionsBuilder.buildTransactions()
PlaceTransactions.placeAll()