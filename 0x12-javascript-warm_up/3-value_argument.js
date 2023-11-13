#!/usr/bin/node

/**
 * This script prints the first argument passed to it
 * or 'No argument' if it is called without
 */
for (const index in process.argv) {
  if (parseInt(index) === 2) {
    console.log(process.argv[index]);
    process.exit();
  }
}
console.log('No argument');
