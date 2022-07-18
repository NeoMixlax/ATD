def sort(matrix):
    for k in range(len(matrix)):
        for i in range(len(matrix)-1):
            if matrix[i][1] > matrix[i+1][1]:
                auxMatrix = matrix[i]
                matrix[i] = matrix[i+1]
                matrix[i+1] = auxMatrix