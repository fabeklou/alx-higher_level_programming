#!/usr/bin/node

const request = require('request');

try {
  const URL = process.argv[2];
  request(URL, (error, response) => {
    if (error) throw error;
    console.log(`code: ${response.statusCode}`);
  });
} catch (error) {
  console.error(error);
}
