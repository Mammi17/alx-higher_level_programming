#!/usr/bin/node
/**
 * add - Computes the sum of 2 numbers.
 * @x - The first number.
 * @y - The second number.
 * Return: The sum of the 2 numbers.
 */

function add (x, y) {
  return x + y;
}

console.log(
  add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]))
);
