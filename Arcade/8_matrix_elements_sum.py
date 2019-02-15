def matrixElementsSum(matrix):
    free_columns = []
    price = 0
    for row in matrix:
        for i in range(len(row)):
            if row[i] == 0:
                free_columns.append(i)
            elif i not in free_columns:
                price += row[i]
            else:
                continue
    return price