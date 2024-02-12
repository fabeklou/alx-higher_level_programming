#!/usr/bin/node

const intArr = process.argv.slice(2).map(item => parseInt(item));

if (intArr.length <= 1) console.log(0);
else console.log(intArr.sort((a, b) => b - a)[1]);
