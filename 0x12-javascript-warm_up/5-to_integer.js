#!/usr/bin/node
const My_num = Math.floor(Number(process.argv[2]));
console.log(isNaN(My_num) ? 'Not a number' : `My number: ${My_num}`);
