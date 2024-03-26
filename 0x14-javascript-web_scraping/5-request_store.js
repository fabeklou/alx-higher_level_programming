#!/usr/bin/node

const fs = require('fs');
const request = require('request');

try {
  const URL = process.argv[2];
  const FILE = process.argv[3];
  const options = { encoding: 'utf8', flag: 'w' };

  request(URL, (error, response, body) => {
    if (error) throw error;

    fs.writeFile(FILE, body, options, (error) => {
      if (error) throw error;
    });
  });

} catch (error) {
  console.error(error);
}
