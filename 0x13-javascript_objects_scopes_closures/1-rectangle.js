#!/usr/bin/node

module.exports = class Rectangle {
  /**
   * The constructor of the Rectangle class - initializes a new
   * Rectangle object
   *
   * @param {number} w - width of the rectangle
   * @param {number} h - height of the rectangle
   */
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
