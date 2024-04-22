#!/usr/bin/node
const args = process.argv.slice(2);
if (args[0] === undefined || args.length === 1) {
  console.log(0);
} else {
  let max = parseInt(args[0], 10);
  let max2 = parseInt(args[0], 10);
  for (let i = 1; i < args.length; i++) {
    const value = parseInt(args[i], 10);
    if (value > max) {
      max = value;
    }
  }

  for (let i = 1; i < args.length; i++) {
    const value = parseInt(args[i], 10);
    if (value === max) {
      continue;
    } else if (max2 < value) { max2 = value; }
  }
  console.log(max2);
}
