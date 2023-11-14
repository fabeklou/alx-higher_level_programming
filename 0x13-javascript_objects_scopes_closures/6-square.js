#!/usr/bin/node

/**
 * This module defines a Square class (child of the Rectangle class),
 * blueprint for square objects
 */

const FirstSquare = require('./5-square');

module.exports = class Square extends FirstSquare {
  /**
   * The constructor of the Square class - same as the
   * constructor of the Rectangle class with:
   *    size = width = height
   *
   * @param {number} size - size of the Square object
   */
  constructor (size) {
    super(size, size);
  }

  /**
   * prints a visual representation of a Square object
   * using the provided character 'C' or 'X' otherwise
   *
   * @param {string} c - the character to print the Square object with
   */
  charPrint (c = 'X') {
    let line = '';

    for (let x = 0; x < this.width; x++) {
      line += c;
    }

    for (let y = 0; y < this.height; y++) {
      console.log(line);
    }
  }
};
