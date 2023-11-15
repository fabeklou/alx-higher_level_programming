#!/usr/bin/node

/**
 * This script concats 2 files
 */

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const dataArr = [];

if (!(fs.existsSync(fileA) &&
      fs.statSync(fileA).isFile &&
      fs.existsSync(fileB) &&
      fs.statSync(fileB).isFile &&
      fileC !== undefined)) {
  process.exit();
}

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    throw err;
  }
  dataArr.push(dataA);
});

fs.readFile(fileB, 'utf8', (err, dataB) => {
  if (err) {
    throw err;
  }
  dataArr.push(dataB);

  fs.writeFile(fileC, `${dataArr[0]}\n${dataArr[1]}\n`, (err) => {
    if (err) {
      throw err;
    }
  });
});
