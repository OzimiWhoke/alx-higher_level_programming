#!/usr/bin/node
const My_Num = Math.floor(Number(process.argv[2]));
console.log(isNaN(My_Num) ? 'Not a number' : `My number: ${My_Num}`);
