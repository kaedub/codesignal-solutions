function isLetter(c) {
    return c[i].toLowerCase() !== c[i].toUpperCase();
}

function isNumber(n) {
    return !isNaN(parseInt(n,10));
}

function isLetter(c) {
    return c.toLowerCase() !== c.toUpperCase();
}

function hasWhitespace(s) {
    return s.indexOf(' ') >= 0;
}



function variableName(name) {
    var firstchar = name.toLowerCase().charCodeAt(0) - 96;
    
    if (isLetter(name[0]) || name[0] === '_') {
        console.log(name[0],'is a valid starting character');
    } else {
        return false;
    }
    for (var i = 1; i < name.length; i++) {
        console.log('val',name[i],'.')
        if ((isLetter(name[i]) || isNumber(name[i])) || name[i] === '_') {
            console.log(name[i],'is a valid character');
        } else {
            console.log(name[i],'is not a letter, number, or underscore');
            return false;
        }
    }
    return true;
}
