#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  const value = dict[key];

  if (!(value in newDict)) newDict[value] = [];
  newDict[value].push(key);
}

console.log(newDict);
