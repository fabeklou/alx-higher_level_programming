#!/usr/bin/node

/**
 * This module defines a function that converts
 * a number from base 10 to another base
 */

/**
 * Converts a number from base 10 to another base passed as argument
 * using closure
 *
 * @param {number} base - the base in which the value
 *    is to be converted
 *
 * @returns {string} - the number converted to another base (string)
 */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
