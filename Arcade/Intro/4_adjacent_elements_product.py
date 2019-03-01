def adjacentElementsProduct(inputArray):
    product = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        next = inputArray[i] * inputArray[i+1]
        if next > product:
            product = next
    return product
