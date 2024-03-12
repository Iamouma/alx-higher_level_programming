#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let n = '';
      for (let j = 0; j < this.width; j++) {
        n += c;
      }
      console.log(n);
    }
  }
}

module.exports = Square;
