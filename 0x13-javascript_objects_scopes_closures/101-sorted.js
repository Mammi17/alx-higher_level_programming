#!/usr/bin/node

const dict = require('./101-data.js');
const ndict = {};
const dct = dict.dict;
let nList = [];
for (const a in dct) {
  const val = dct[a];
  for (const b in dct) if (dct[b] === val) nList.push(b);
  ndict[val] = nList;
  nList = [];
}
console.log(ndict);

