#!/usr/bin/node

const firstArg = process.argv[2];
const myNumber = parseInt(firstArg);

if (myNumber) console.log(`My number: ${myNumber}`);
else console.log('Not a number');
