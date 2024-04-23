#!/usr/bin/node
const fs = require('fs');
const file = process.argv.slice(2);

const contentOfFile1 = fs.readFileSync(file[0], 'utf8');
const contentOfFile2 = fs.readFileSync(file[1], 'utf8');
fs.writeFileSync(file[2], contentOfFile1 + contentOfFile2);
