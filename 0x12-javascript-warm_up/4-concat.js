#!/usr/bin/node
// a script that prints two arguments passed to it
// in the following format: “ is ”.

const arg = process.argv[2];
const args = process.argv[3];

console.log(arg + ' is ' + args);
