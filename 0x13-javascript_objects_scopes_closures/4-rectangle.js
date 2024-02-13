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

  /**
   * prints a visual representation of a Rectangle object
   * using the character 'X'
   */
  print () {
    const char = 'X';
    const width = char.repeat(this.width);
    for (let i = 0; i < this.height; i++) console.log(width);
  }

  /**
   * exchanges the <width> and the <height> values of the rectangle
   */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /**
   * multiplies the <width> and the <height> of the rectangle by 2
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
