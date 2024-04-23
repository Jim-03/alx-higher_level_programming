#!/usr/bin/node
let numberOfArgument = 0;
exports.logMe = function (item) {
  console.log(`${numberOfArgument}: ${item}`);
  numberOfArgument++;
};
