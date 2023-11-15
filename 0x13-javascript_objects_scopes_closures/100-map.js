#!/usr/bin/node

/**
 * This script imports an array and computes a new array
 */

const initialList = require('./100-data').list;

const newList = initialList.map((val, idx) => val * idx);

console.log(initialList);
console.log(newList);
