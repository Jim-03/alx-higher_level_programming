#!/usr/bin/node
function fact (x) {
  if (x <= 1) {
    return 1;
  }
  const result = x;
  return result * fact(x - 1);
}

const args = process.argv.slice(2);
const x = parseInt(args[0], 10);
if (isNaN(x)) {
  console.log(1);
} else {
  console.log(fact(x));
}
