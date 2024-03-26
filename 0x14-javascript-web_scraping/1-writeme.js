#!/usr/bin/node

const fs = require('fs');

try {
  const path = process.argv[2];
  const content = process.argv[3];
  const options = { encoding: 'utf8', flag: 'w' };

  fs.writeFile(path, content, options, (error) => {
    if (error) throw error;
  });
} catch (error) {
  console.error(error);
}
