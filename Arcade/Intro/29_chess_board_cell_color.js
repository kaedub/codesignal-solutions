function letterToPos(c) {
    return c.charCodeAt(0) - 65
}

function chessBoardCellColor(cell1, cell2) {
    function isBlack(cell) {
        if (1 + parseInt(cell[1]) % 2 === 1 + letterToPos(cell[0]) % 2) return true;
        return false;
    }
    return isBlack(cell1) === isBlack(cell2);
}
