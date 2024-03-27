#!/usr/bin/node

const request = require('request');

try {
  const URL = process.argv[2];
  const ID = '18';
  request(URL, (error, response, body) => {
    if (error) throw error;
    const DATA = JSON.parse(body);
    let count = 0;
    for (const result of DATA.results) {
      for (const characterLink of result.characters) {
        const tokens = characterLink.split('/');
        if (tokens[tokens.length - 2] === ID) count += 1;
      }
    }
    console.log(count);
  });
} catch (error) {
  console.error(error);
}
