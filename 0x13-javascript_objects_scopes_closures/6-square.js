#!/usr/bin/node

const SquareParent = require('./5-square.js');

module.exports = class Square extends SquareParent {
  /**
   * prints a visual representation of a square object
   * using a given character or 'X' if no argument is given
   *
   * @param {string} c - the character to print the Square object with
   */
  charPrint (c = 'X') {
    const char = c;
    const width = char.repeat(this.width);
    for (let i = 0; i < this.height; i++) console.log(width);
  }
};
