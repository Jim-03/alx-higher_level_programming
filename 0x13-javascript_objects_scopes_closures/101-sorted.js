#!/usr/bin/node
const dictionary = require('./101-data').dict;
const newDict = {};

for (const [Id, occurence] of Object.entries(dictionary)) {
  if (newDict[occurence]) {
    newDict[occurence].push(Id);
  } else {
    newDict[occurence] = [Id];
  }
}

console.log(newDict);
