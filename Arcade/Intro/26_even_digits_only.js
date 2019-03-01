function evenDigitsOnly(n) {
    var a = n.toString().split('');
    for (let e of a) 
        if (e % 2 !== 0) return false;
    return true;
}
