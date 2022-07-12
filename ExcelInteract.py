import openpyxl as xl 
from openpyxl.worksheet.table import Table, TableStyleInfo

# Getting the Excel's Workbook
archivo = xl.load_workbook(r"C:\Users\nicor\OneDrive - UNIVERSIDAD INDUSTRIAL DE SANTANDER\Desktop\Financial\NeoCrypto.xlsx")

def modifyCellValue(row: int, column: int, value, sheet):
    hoja = archivo[sheet]
    hoja.cell(row, column).value = value
            
def modifyCellValueDate(row: int, column: int, value, sheet):
    hoja = archivo[sheet]
    year = value.split("-")[0]
    monthh = value.split("-")[1]
    day = value.split("-")[2]
    hoja.cell(row, column).value = "=DATE({}, {}, {})".format(year, monthh, day)

def modifyCellValueHour(row: int, column: int, value, sheet):
    hoja = archivo[sheet]
    hoja.cell(row, column).value = value
    hoja.cell(row, column).number_format = "[$-x-systime]h:mm:ss AM/PM"

def saveWb():
    archivo.save(r"C:\Users\nicor\OneDrive - UNIVERSIDAD INDUSTRIAL DE SANTANDER\Desktop\Financial\NeoCrypto.xlsx")

def modifyTable(cell1, cell2, sheet, name):
    hoja = archivo[sheet]
    column1= cell1[0]
    row1= cell1[1]
    column2= cell2[0]
    row2= cell2[1]
    hoja.tables[name].ref = "{}{}:{}{}".format(column1, row1, column2, row2)
