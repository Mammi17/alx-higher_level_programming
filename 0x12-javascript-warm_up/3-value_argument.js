#!/usr/bin/node
// a script that prints the first argument passed.

const arg0 = process.argv[2];

console.log(arg0 !== undefined ? arg0 : 'No argument')
