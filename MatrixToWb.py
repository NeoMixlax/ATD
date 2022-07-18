import ExcelInteract

def placeMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j==1: 
                ExcelInteract.modifyCellValue(i+3, j+2, "Órdenes", matrix[i][j], "d/mm/yyyy") 
            else:
                ExcelInteract.modifyCellValue(i+3, j+2, "Órdenes", matrix[i][j])