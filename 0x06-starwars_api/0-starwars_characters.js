#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit();
}
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request({ url, json: true }, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

request({ url, json: true }, async function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const characters = body.characters;
  for (const character of characters) {
    try {
      const characterData = await makeRequest(character);
      console.log(characterData.name);
    } catch (error) {
      console.error('Error fetching character data:', error);
    }
  }
});
