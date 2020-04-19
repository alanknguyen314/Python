# Python Data Types
# Python has these data types built in by default, in these categories:

# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# In python, you don't have to declare a data type for a variable. The datatype is automatically set.

# 1. The type() function
# This function is used to get the data type of a variable.
name = "Nguyen"
print(type(name)) # Prints out <class "str">

# 2. The isinstance() function
# This function will check whether a variable belongs to a particular class and return a boolean value.
name1 = "Harry"
print(isinstance(name, int)) # Prints out "False" since name1 isn't an integer.

# 3. Python Casting
# This means to convert a variable's data type from one to another.
# Casting is done using constructor functions

    # 3.1 The int() function
    # Constructs an integer number from an integer literal, a float literal, or a string literal (providing that the string
    # represents a whole number)

    # 3.2 The float() function
    # Constructs a float number from an integer literal, a float literal or a string literal 
    # (providing the string represents a float or an integer)

    # 3.3 The str() function
    # Constructs a string from a wide variety of data types, including strings, integer literals and float literals



