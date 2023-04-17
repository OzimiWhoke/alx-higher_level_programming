#!/usr/bin/node
// Import Square class from 5-square.js
const BaseSquare = require('./5-square');

// Define Square class that inherits from BaseSquare
class Square extends BaseSquare {
  charPrint(c) {
    // Set default character to X if c is undefined
    if (!c) {
      c = 'X';
    }

    // Print square using specified character
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

// Export Square class
module.exports = Square;
