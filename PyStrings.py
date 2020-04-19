# Python Text 
# str

# String literals in python are surrounded by either single quotation marks, or double quotation marks. Multi-line Strings
# are surrounded by three quotation marks. 
# Strings are a type of array, which means that we can index it, character by character.
# String literals are immutable (can't be change)

print("Hello!")
print("""Hey there buddy!
You're great! """)

# 1. String Character Index
name = "Nguyen"
print(name[0]) # Prints out "N" because the 0th index of the variable name is "N"

# 2. String Slicing
# Remember slicing will always include the starting index but never include the ending index (exclusive)
statement1 = "Mr. Scott is hungry"
print(statement1[13:19]) # Prints out "hungry"

# 3. String negative Slicing
# This is also slicing, but starting from the end of the string.
statement2 = "Nguyen"
print(statement2[-6:-1]) # Prints out "Nguye"

# 4. The len() function
# This function is used to return the length of a string
statement3 = "Nguyen K. Nguyen"
print(len(statement3)) # The length is 16

# 5. The strip() method
# The strip() method removes any white space from the beginning to the end.
statement4 = "            NGUYEN            "
print(statement4.strip())

# A good reminder of the difference between a function and a method: A function will have the overall syntax as [function(argument)]
# where a method will have the overall syntax as [argument.method()]

# 6. The lower() and upper() methods
# The lower() method returns string in lowercase; the upper() method returns string in uppercase
name2 = "Washington"
print(name2.lower())
print(name2.upper())

# 7. The replace() method
# The replace() method will replace a string with another string
name3 = "Hello, World!"
print(name3.replace("Hello,", "Goodbye,"))

# 8. The split() method
# THe split() method will split the string if it finds instance of the separator. The remaining fractures will be put in an array.
name4 = "Hello, World, Nguyen!"
print(name4.split(",")) # Split out "," 

# 9. String Checking with keywords "in" and "not in"
# A phrase can be checked if it's in a string or not.
name5 = "Theodore Roosevelt"
roose_in_name5 = "Roose" in name5
doree_in_name5 = "Doore" in name5
print(roose_in_name5) #This will return True since "Roose" does appear in name5
print(doree_in_name5) # This will return False since "Doree" isn't in name5

# 10. String concatenation
# String can be added to each other using + sign
first_name = "Alan"
last_name = "Nguyen"
full_name = first_name + last_name
print(full_name)

# 11. String Format with the format() method
# The format() method will take in an argument and format them, then place them in the string where the placeholder "{}" are
# The numbers in the placeholder specify the position of the argument that's being placed in.
nguyen_age = 19
nguyen_name = "Nguyen Khoi Nguyen"
nguyen_statement = "My name is {0}, and I'm {1} years old"
print(nguyen_statement.format(nguyen_name, nguyen_age))

# 12. Double Quotes in String
# The double quotes in a string can only be represented by a double slash.
statement5 = "I'm that one \"nerdy\" kid at school"
print (statement5) # Prints "I'm that one "nerdy" kid at school"

# External String Manipulating methods.
# Include later.





 





