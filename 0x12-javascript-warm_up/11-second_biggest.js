#!/usr/bin/node
//  a script that searches the second biggest
//  integer in the list of arguments.

const args = process.argv.slice(2);
let nextM = 0;

if (args.length > 1) {
  const intger = args.map(Number);
  intger.sort((a, b) => b - a);
  nextM = intger[1];
}

console.log(nextM);
