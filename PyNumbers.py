# Python Numbers
# int, float and complex 
# Python numbers are mutable, which means that they can be changed over time.

import random

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 10
print(x)

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals. 
# Float can also be scientific numbers with an "e" to indicate the power of 10.
y = 25.5
y1 = 35e3 # prints "35000.0"
print(y)
print(y1)

# Complex numbers are written with a "j" as the imaginary part:
z = 5 + 10j
print(z)

# 1. Type Conversion
# You can convert from one type of number to another with the int(), float() and complex() methods
# You can't convert from complex to int or float easily if they have imaginary number(s)

a = 15
b = 10.5
c = 10 + 15j

a1 = float(a)
b1 = int(b)
print(a, b)

# Python does not have a random() function to make a random number, but Python has a built-in module called random 
# that can be used to make random numbers:
print(random.randrange(1, 10)) # Print a random number in the range 1 - 9



