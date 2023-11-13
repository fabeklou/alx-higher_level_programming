#!/usr/bin/node

/**
 * This script compute and prints a factorial
 * example <3>: 6
 */
const num = parseInt(process.argv[2]);

function facto (value) {
  if (isNaN(value) || value === 0 || value === 1) {
    return 1;
  }
  return value * facto(value - 1);
}

console.log(facto(num));
