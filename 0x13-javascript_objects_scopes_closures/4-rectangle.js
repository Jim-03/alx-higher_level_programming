#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w === 0 || h === 0 || w === undefined || h === undefined || w < 0 || h < 0) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let down = 0; down < this.height; down++) {
      let row = '';
      for (let side = 0; side < this.width; side++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
