#!/usr/bin/node
const args = process.argv.slice(2);
const x = parseInt(args[0], 10);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < x; count++) {
    console.log('C is fun');
  }
}
