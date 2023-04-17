#!/usr/bin/node
const dict = require('./101-data.js');

const newDict = {};
for (const [userId, occurrences] of Object.entries(dict)) {
  if (newDict[occurrences.length] === undefined) {
    newDict[occurrences.length] = [userId];
  } else {
    newDict[occurrences.length].push(userId);
  }
}
console.log(newDict);
