#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movie = JSON.parse(body);
      const characters = movie.characters;

      if (characters && characters.length > 0) {
        characters.forEach((characterURL) => {
          request.get(characterURL, (charError, charResponse, charBody) => {
            if (charError) {
              console.error(charError);
            } else {
              const character = JSON.parse(charBody);
              console.log(character.name);
            }
          });
        });
      } else {
        console.log('No characters found for this movie.');
      }
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
