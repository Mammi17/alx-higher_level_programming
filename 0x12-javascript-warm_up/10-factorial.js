#!/usr/bin/node
/**
 * factorial - Computes the factorial of a number.
 * @numb - The number.
 * Return: The factorial of the number.
 */

function factorial (numb) {
  if (Number.isNaN(numb) || (numb <= 0)) {
    return 1;
  } else {
    return numb * factorial(numb - 1);
  }
}

console.log(factorial(Number.parseInt(process.argv[2])));
