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
}

module.exports = Rectangle;
