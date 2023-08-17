#!/usr/bin/node
// a script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer

const numb = Number.parseInt(process.argv[2]);

console.log(Number.isNaN(numb) ? 'Not a number' : 'My number: ' + numb);
