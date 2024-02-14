#!/usr/bin/node

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
};
