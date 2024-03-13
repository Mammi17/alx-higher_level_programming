#!/usr/bin/node
// Rotate and Double the width and height of the Rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (a) {
    a = 'X';
    for (let b = 0; b < this.height; b++) {
      console.log(a.repeat(this.width));
    }
  }
};

