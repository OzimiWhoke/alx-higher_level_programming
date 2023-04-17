#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 5) {
  console.log('Usage: node concat.js <file1> <file2> <output>');
  process.exit(1);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const output = process.argv[4];

try {
  const data1 = fs.readFileSync(file1, 'utf8');
  const data2 = fs.readFileSync(file2, 'utf8');
  fs.writeFileSync(output, data1 + data2);
  console.log(`Concatenated ${file1} and ${file2} into ${output}`);
} catch (err) {
  console.error('Error:', err);
}
