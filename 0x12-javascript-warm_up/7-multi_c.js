#!/usr/bin/node

const str = 'C is fun';
const count = parseInt(process.argv[2]);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) console.log(str);
}
