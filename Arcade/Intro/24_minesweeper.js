function isCell(cell) {
    return cell != undefined;
}

function minesweeper(matrix) {
    y_len = matrix.length;
    x_len = matrix[0].length;
    var arr = []; 
    for (let y = 0; y < y_len; y++) arr.push(Array(x_len).fill(0));
    
    for (let y = 0; y < y_len; y++) {
        for (let x = 0; x < x_len; x++) {
            if (matrix[y][x] === true) {
                for (let d = x-1; d <= x+1; d++) {
                    if (y < y_len-1 && isCell(arr[y+1][d])) arr[y+1][d]++;
                    if (y > 0 && isCell(arr[y-1][d])) arr[y-1][d]++;
                    if (d !== x && isCell(arr[y][d])) arr[y][d]++;                    
                }                   
            }               
        }
    }
    return arr;
}
