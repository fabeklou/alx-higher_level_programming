#!/usr/bin/node

/**
 * Prints the number of arguments already printed and
 * the new argument value
 *
 * @param {string} item - the argument value to be printed
 */
exports.logMe = function (item) {
  if (typeof this.count === 'undefined') this.count = 0;
  else this.count++;
  console.log(`${this.count}: ${item}`);
};
