#!/usr/bin/node
// that concats 2 files.

require('process');
const ft = require('fs');
const argv = process.argv;
ft.readFile(argv[2].toString(), 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  ft.writeFile(argv[4].toString(), data, (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
ft.readFile(argv[3].toString(), 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  ft.appendFile(argv[4].toString(), data, (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});

