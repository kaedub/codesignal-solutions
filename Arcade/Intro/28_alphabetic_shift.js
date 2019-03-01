function shiftChar(c) { 
    return String.fromCharCode((c.charCodeAt(0)-96)%26+ 97);
}

function alphabeticShift(inputString) {
    return inputString.split('').map(shiftChar).join('');
}
