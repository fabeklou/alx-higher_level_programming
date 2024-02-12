#!/usr/bin/node

const num = parseInt(process.argv[2]);

function facto (num) {
  if (isNaN(num) || num <= 1) return 1;
  return num * facto(num - 1);
}

console.log(facto(num));
