#!/usr/bin/node

const list = require('./100-data.js');
console.log(list.list);
let a = 0;
const nList = list.list.map(x => x * a++);
console.log(nList);

