#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
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
};
