#!/usr/bin/node

/**
 * This script prints a message depending of the number
 * of arguments passed
 *
 * if process.argv === 0:
 *      'No argument'
 * if process.argv === 1:
 *      'Argument found'
 * if process.argv >= 2:
 *      'Arguments found'
 */
const argCount = process.argv.length - 2;

if (argCount === 0) {
  console.log('No argument');
} else if (argCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
