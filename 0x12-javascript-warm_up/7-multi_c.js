#!/usr/bin/node

/**
 * This script prints <x> time 'C is fun'
 * <x>: the first argument of the script
 */
const firstArg = parseInt(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < firstArg; count++) {
    console.log('C is fun');
  }
}
