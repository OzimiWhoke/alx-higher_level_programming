#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print(f"{number} is Zero")
