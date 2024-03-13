#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (a) {
    if (a === undefined) {
      a = 'X';
    }
    for (let b = 0; b < this.height; b++) {
      console.log(a.repeat(this.width));
    }
  }
}

module.exports = Square;

