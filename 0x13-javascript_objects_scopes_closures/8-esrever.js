#!/usr/bin/node

/**
 * Returns a reversed version of the list passed to it
 *
 * @param {Array} list - the list to be reversed
 *
 * @returns {Array} - the reversed version of <list>
 */
exports.esrever = function (list) {
  const rev = [];
  const len = list.length;
  for (let i = len - 1; i >= 0; --i) rev.push(list[i]);
  return rev;
};
