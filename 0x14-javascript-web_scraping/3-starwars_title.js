#!/usr/bin/node

const request = require('request');

try {
  const episode = process.argv[2];
  const URL = `https://swapi-api.alx-tools.com/api/films/${episode}`;
  request(URL, (error, response, body) => {
    if (error) throw error;
    console.log(`${JSON.parse(body).title}`);
  });
} catch (error) {
  console.error(error);
}
