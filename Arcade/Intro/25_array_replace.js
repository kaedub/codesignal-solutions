function arrayReplace(inputArray, elemToReplace, substitutionElem) {
    for (let i = 0; i < inputArray.length; i++) 
        if (inputArray[i] === elemToReplace) inputArray[i] =substitutionElem;
    return inputArray
}
