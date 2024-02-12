#!/usr/bin/node

const size = parseInt(process.argv[2]);
const char = 'X';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const line = char.repeat(size > 0 ? size : 0);
  for (let i = 0; i < size; i++) console.log(line);
}
