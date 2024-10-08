#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(endPoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
