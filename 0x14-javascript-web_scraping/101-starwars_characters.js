#!/usr/bin/node

const request = require('request');

const fetchCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      resolve(JSON.parse(body).name);
    });
  });
};

const asyncFetch = async (urlArray) => {
  try {
    for (const url of urlArray) {
      const result = await fetchCharacter(url);
      console.log(result);
    }
  } catch (error) {
    console.error(error);
  }
};

try {
  const ID = process.argv[2];
  const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;

  request(URL, (error, response, body) => {
    if (error) throw error;
    const characters = JSON.parse(body).characters;
    asyncFetch(characters);
  });
} catch (error) {
  console.error(error);
}
