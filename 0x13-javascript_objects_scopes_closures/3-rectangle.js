#!/usr/bin/node

/**
 * This module defines a Rectangle class, blueprint for
 * rectangle objects
 */

module.exports = class Rectangle {
  /**
   * The constructor of the Rectangle class - initializes a new
   * Rectangle object
   *
   * @param {number} w - width of the rectangle
   * @param {number} h - height of the rectangle
   *
   * description - a empty Rectangle object is created if
   * either <w> or <h> is not valid (less or equal to 0)
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * prints a visual representation of a Rectangle object
   * using the character 'X'
   */
  print () {
    let line = '';

    for (let x = 0; x < this.width; x++) {
      line += 'X';
    }

    for (let y = 0; y < this.height; y++) {
      console.log(line);
    }
  }
};
