#!/usr/bin/node

/**
 * This module defines a function that shows the number
 * of arguments already printed and the new argument value
 */

/**
 * Prints the number of arguments already printed and
 * the new argument value
 *
 * @param {string} item - the argument value to be printed
 */
exports.logMe = function (item) {
  /* functions are objects so the can have properties */
  if (typeof this.count === 'undefined') {
    this.count = 0;
  }

  console.log(`${this.count}: ${item}`);
  this.count++;
};
