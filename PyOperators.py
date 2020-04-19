# Python Operators

# Operators are used to perform operations on variables and values. There are lots of different types of operators,
# categorized as follows:

# - Arithmetic Operators
# - Assignment Operators
# - Comparision Operators
# - Logical Operators
# - Identity Operators
# - Membership Operators
# - Bitwise Operators

# 1. Arithmetic Operators
# Arithmetic Operators are used with numeric values to perform common mathematical operations.
x = 5
y = 10
ans1 = x + y # Addition 
ans2 = x - y # Subtraction
ans3 = x * y # Multiplication
ans4 = x / y # Division
ans5 = x % y # Modulus
ans6 = x ** y # Exponentiation
ans7 = x // y # Floor Division (This is division and then round down)
print(ans1, ans2, ans3, ans4, ans5, ans6, ans7)

# 2. Assignment Operators
# Assignment operators are used to assign values to variables. THere are lots of cumulative assignment operators, which performs an arithmetic
# operation on the variable and then allow it to be updated immediately after. These cumulative assignment operators are often times +=, -=, *=,
# /= and more, usually the combination of an arithmetic operator and the assignment operator. x += 1 means x = x + 1

# 3. Comparison Operators
# Comparison Operators are used to compare two values.
print(5 == 5) # Equal to
print(5 != 7) # Not equal to
print(5 < 6) # Smaller than
print(5 > 3) # Greater than
print(5 <= 5) # Smaller or equal to
print(5 >= 5) # Greater or equal to

# 4. Logical Operators
# Logical Operators are used to combine conditional statements
print((5 == 5) and (5 < 3)) # and operator, returns True if both conditions are True.
print((5 == 5) or (5 < 3)) # or operator, returns true when one of the statement is True.
print(not(5 == 5)) # not operator, reverse the boolean value of the statement

# 5. Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, 
# with the same memory location
a = "Hello World!"
b = "Hello World!"
print(a is b) # Returns True since a and b contain the same thing. 
print(a is not b) # Returns False since a == b == "Hello World!"

# 6. Membership Operators
# Membership operators are used to test if a sequence is present in an object.
name = "Nguyen"
names = ["Washington", "Roosevelt", "Adams"]
print ("Ngu" in name) # Returns True as "Ngu" is in "Nguyen"
print ("Eisenhower" not in names) # Returns True as "Eisenhower" isn't in the list "names"

# 7. Bitwise Operators
# Bitwise operators are used to compare binary numbers

# - "&" is AND operator
# - "|" is OR operator
# - "^" is XOR operator
# - "~" is NOT operator
# - ">>" is Signed Right Shift operator, shift left by pushing zeroes in from the right, and let the leftmost bits fall off
# - "<<" is Signed Left Shift operator, shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off






