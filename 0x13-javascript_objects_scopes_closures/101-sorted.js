#!/usr/bin/node

/**
 * This script imports a dictionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence
 */

const initialDict = require('./101-data').dict;
const newDict = {};

for (const key in initialDict) {
  const value = initialDict[key];

  if (!(value in newDict)) {
    newDict[value] = [];
  }

  newDict[value].push(key);
}

console.log(newDict);
