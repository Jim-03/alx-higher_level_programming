#!/usr/bin/node
const args = process.argv.slice(2);
const size = parseInt(args[0], 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let down = 0; down < size; down++) {
    let row = '';
    for (let side = 0; side < size; side++) {
      row += 'X';
    }
    console.log(row);
  }
}
