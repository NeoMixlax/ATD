# ATD
Automated Trading Daily

## Description
This project was made for managing an automated trading daily in an Excel's workbook, it provides 2 main funcionalities for this purpose:
1. Get all your trades from all your diferent coins in binance and sort the data in a table.
2. Get the current value of all the coins you've ever traded in order and sort the data in another table. 

The purpose this code was created is not only to get all your trades, but also get the binance value of all that coins for you to take a view of your current economical status.

## Languages
- Python.

## Libraries
- [python-binance](https://python-binance.readthedocs.io/en/latest/).
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/).

## Developing enviroment used
- Visual Studio Code (coding).
- Windows CMD (running/testing).

## Installation
First to say, the actual repository is uncompleted, then it won't work if to try running the main file.

If you check the source code you'll notice there's a Credenciales.py file missing, that's because there's where are stored the API credentials. In order to adapting your own code you'll have to create this file by yourself adding the 'api_key' and 'secret_key' variables. Also you need to specify the filw the code will modify.

On the other hand, I created this code for being runned in my personal PC, then, the way I run it is through a virtual enviroment from which I had to install python-binance and openpyxl libraries, previously intalled python on my device. These are the steps you'll have to follow if you want to run it the way I do:
1. Create a new Excel Workbook where you're gonna manage all your crypto stuff.
2. Create a table placing a header for each "Transaccion" attribute.
3. Create another table placing a heading according to "PlaceValues" method in "PlaceTransactions.py".
4. Set your tables ranges in the "PlaceTransactions.py" methods.
4. Copy the file address and paste it in the "archivo" variable inn "ExcelInteract.py" file.
5. Create a file named "Credenciales.py" in the same folder we're working on and define your "api_key" and "secret_key" variables.

## Notes
- Sometimes when you run the code you get a request timeout error, the reasons may suggest that you gotta improve your internet connection or maybe the address is quite crowded and you gotta try it again in a bit.
- I'm kind of newbie using python and this is my first project on it. Surely I got a lot of things that could be significally improved on my code, so please feel free to make me know what could I done better and please modify my code for making something great for us all :D.
- Please **NEVER** code when you are tired :).

## Credits
This project is based on [this](https://www.youtube.com/watch?v=wEz05w1d3nE).

## Updates
### 28/07/2022
- The program was completely restructured in order to develop it using OOP. This update makes the code not only better in terms of  improving the quality of it but also making it easier to understand.

- Some files were removed and added following the OOP logical. 

- 2 extra rows were added to the Values table, total amount of each coin and what it represents in BTC.

- The entire VE(virtual enviroment) was added to the repository in order to improve the understanding of the code.

- The Binance API address was modified in the python-binance librarie installed in the VE, the objective was improving the requesting flow using a less crowded address minimizing the request timeout errors.