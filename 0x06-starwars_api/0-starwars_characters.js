#!/usr/bin/node

const request = require('request')

request('https://swapi-api.hbtn.io/api/fils/' + process.argv[2], function(err, res, body) {
  if (err) throw err;
	const characterNames = JSON.parse(body).character;
	exactOrder(characterNames, 0);
});

const exactOrder = (characterNames, x) => {
  if (x === characterNames.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(characterNames, x + 1);
  });
