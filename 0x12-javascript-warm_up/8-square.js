#!/usr/bin/node

/**
 * This script prints a square based on his argument
 * example <2>: xx
 *              xx
 */
const firstArg = parseInt(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  let width = '';

  for (let x = 0; x < firstArg; x++) {
    width += 'X';
  }

  for (let y = 0; y < firstArg; y++) {
    console.log(width);
  }
}
