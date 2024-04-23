#!/usr/bin/node
exports.esrever = function (list) {
  for (let element = 0; element < Math.floor(list.length / 2); element++) {
    const newVal = list[element];
    list[element] = list[list.length - 1 - element];
    list[list.length - 1 - element] = newVal;
  }
  return list;
};
