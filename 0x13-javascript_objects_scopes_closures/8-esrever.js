#!/usr/bin/node

/**
 * This module defines a function that returns
 * the reversed version of a list
 */

/**
 * Returns a reversed version of the list passed to it
 *
 * @param {Array} list - the list to be reversed
 *
 * @returns {Array} - the reversed version of <list>
 */
exports.esrever = function (list) {
  const reverseList = [];

  for (const element of list) {
    reverseList.unshift(element);
  }

  return reverseList;
};
