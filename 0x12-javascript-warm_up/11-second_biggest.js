#!/usr/bin/node

/**
 * This script finds and prints the second biggest
 * integer in the list of argument passed to it
 */
const argList = process.argv.slice(2);
const argCount = argList.length;

if (argCount === 0 || argCount === 1) {
  console.log(0);
} else {
  const argListInt = [];

  for (const value of argList) {
    argListInt.push(parseInt(value));
  }

  const sortedListDesc = argListInt.sort((a, b) => b - a);
  console.log(sortedListDesc[1]);
}
