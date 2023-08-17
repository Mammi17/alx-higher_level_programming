#!/usr/bin/node
/**
 * square - Prints a square with 'X'.
 * @param {Number} size - The size of the square.
 */

function square (size) {
  if (Number.isNaN(size)) {
    console.log('Missing size');
  } else if (size >= 0) {
    const r = new Array(size);
    for (let a = 0; a < size; a++) {
      r.push('X');
    }
    let rows = new Array(size);
    rows = rows.fill(r.join(''), 0, size);
    console.log(rows.join('\n'));
  }
}

square(Number.parseInt(process.argv[2]));
