#!/usr/bin/node

const fs = require('fs');

try {
  const path = process.argv[2];
  const content = fs.readFileSync(path, 'utf8');
  console.log(content);
} catch (error) {
  console.error(error);
}
