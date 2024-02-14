#!/usr/bin/node

/**
 * Counts and returns the number of occurences of an element in a list
 *
 * @param {Array} list - the Array of elements
 * @param {any} searchElement - the element whose occurrences
 * should be counted
 *
 * @returns {number} - the number of occurences of the <searchElement>
 * founds in the <list>
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const item of list) {
    if (item === searchElement) count++;
  }
  return count;
};
