def sort(matrix):
    for k in range(len(matrix)):
        for i in range(len(matrix)-1):
            if matrix[i][1] > matrix[i+1][1]:
                auxMatrix = matrix[i]
                matrix[i] = matrix[i+1]
                matrix[i+1] = auxMatrix

def ordenarTransacciones(listaDlistas):
    for lista in listaDlistas:
        ordenarTransaccion(lista)

def ordenarTransaccion(tran):
    if len(tran)>=2:
        for k in range(len(tran)):
            for i in range(len(tran)-1):
                if tran[i].fecha > tran[i+1].fecha:
                    auxT = tran[i]
                    tran[i] = tran[i+1]
                    tran[i+1] = auxT 