#!/usr/bin/node

const request = require('request');

try {
  const ID = process.argv[2];
  const URL = 'https://swapi-api.alx-tools.com/api/films/' + ID;

  request(URL, (error, response, body) => {
    if (error) throw error;
    const characters = JSON.parse(body).characters;
    for (const char of characters) {
      request(char, (err, res, bdy) => {
        if (err) throw err;
        console.log(JSON.parse(bdy).name);
      });
    }
  });
} catch (error) {
  console.error(error);
}
