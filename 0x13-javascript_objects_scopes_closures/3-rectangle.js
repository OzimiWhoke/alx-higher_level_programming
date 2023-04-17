#!/usr/bin/node
class Rectangle:
    def __init__(self, w, h):
        if w <= 0 or h <= 0:
            pass  # creating an empty object
        else:
            self.width = w
            self.height = h

    def print(self):
        if hasattr(self, 'width') and hasattr(self, 'height'):
            for i in range(self.height):
                for j in range(self.width):
                    print("X", end="")
                print()
module.exports = Rectangle;
