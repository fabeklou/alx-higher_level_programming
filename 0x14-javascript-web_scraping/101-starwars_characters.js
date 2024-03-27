#!/usr/bin/node

const request = require('request');

const recursiveFetch = (index, urlArray) => {
  if (index === urlArray.length) return;

  request(urlArray[index], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
  });

  recursiveFetch(index + 1, urlArray);
};

try {
  const ID = process.argv[2];
  const URL = 'https://swapi-api.alx-tools.com/api/films/' + ID;

  request(URL, (error, response, body) => {
    if (error) throw error;
    const characters = JSON.parse(body).characters;
    const index = 0;
    recursiveFetch(index, characters);
  });
} catch (error) {
  console.error(error);
}
