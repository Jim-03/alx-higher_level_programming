#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  charPrint (c) {
    let char = '';
    if (c === undefined) {
      char = 'X';
    } else {
      char = c;
    }
    for (let down = 0; down < this.width; down++) {
      let row = '';
      for (let side = 0; side < this.width; side++) {
        row += char;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
