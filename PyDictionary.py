# Python Dictionaries
# A dictionary is a collection which is unordered, changable and indexed. In python, dictionaries are written with 
# curly brackets, and they have keys and values.

cardictionary = {"brand1": "Ford", "brand2": "BMW", "brand3": "Mercedes", "year1": 1994}
print(cardictionary)

# 1. Accessing a Dictionary with keys
# You can access an item of the dictionary by referring to its keyname, inside square brackets.
namedictionary = {"firstpresident": "Washington", "secondpresident": "Adams", "thirdpresident": "Jefferson"}
print(namedictionary["secondpresident"]) # Returns "Adams"

# 2. Accessing a Dictionary with get() method
# You can also access an item with the get method.
namedictionary1 = {"firstpresident": "Washington", "secondpresident": "Adams", "thirdpresident": "Jefferson"}
print(namedictionary1.get("thirdpresident")) # Prints "Jefferson"

# 3. Change Value of a dictionary's key
# A key within a dictionary can be changed by re-assigning to it a different value.
dictionary1 = {"firstpresident": "Washington", "secondpresident": "Adams", "fourthpresident": "Alan K. Nguyen"}
dictionary1["fourthpresident"] = "Madison"
print(dictionary1)

# 4. for loop with Dictionary
# A for loop can be applied to a dictionary in the same way as with lists and tuples.
dictionary2 = namedictionary = {"1st": "Washington", "2nd": "Adams", "3rd": "Jefferson", "4th": "Madison"}

# 4.1 Iteration through keys
for x in dictionary2:
    print(x)

# 4.2 Iteration through values with keys
for x in dictionary2:
    print(dictionary2[x])

# 4.3 Iteration through values with values() method
for x in dictionary2.values():
    print(x)

# 4.4 Iteration through both keys and values with items() method
for x, y in dictionary2.items():
    print(x, y)

# 5. Dictionary Length with len()
# Dictionary length can be found using the len() function.
random_dict = {"name": "Nguyen", "age": "19", "school": "BVIS"}
print(len(random_dict)) # Prints 3

# 6. Adding items into a dictionary with indexing
# Items can be added into a dictionary be addressing the value to a specific index.
dictionary3 = {"name": "Nguyen", "age": "19", "school": "BVIS"}
dictionary3["major"] = "Physics"
print(dictionary3)

# 7. Removing items from a dictionary with pop() method
# Items can be removed from a dictionary by using the pop() method.
dictionary3.pop("school")
print(dictionary3)

# 8. Removing items from a dictionary with popitem() method
# The last inserted item can be removed from a dictionary by using the popitem() method.
dictionary4 = {"name": "Nguyen", "age": "19", "school": "BVIS"}
dictionary4.popitem()
print(dictionary4) # Poped "major: Physics"

# 9. Removing items from a dictionary or the dictionary with the del keyword
# The del keyword can be used to delete an item or the dictionary completely
dictionary5 = {"name": "Nguyen", "age": "19", "school": "BVIS"}
del dictionary5["age"]
print(dictionary5)

# 10. Removing every items from a dictionary with the clear() method.
# The clear() method is used to clear every items in the dictionary.
dictionary6 = {"name": "Nguyen", "age": "19", "school": "BVIS"}
dictionary6.clear()
print(dictionary6)

# 11. Copy a Dictionary with copy() method
# In order to copy a new dictionary, we must not reference the dictionary from one to another as
# in dict1 = dict2, since any changes in dict1 will be copied into dict2 (reference.) Therefore,
# we must use the copy() method.
dictionary7 = {"name": "Nguyen", "age": "19", "school": "BVIS"}
dictionary8 = dictionary7.copy()
dictionary7.clear()
print(dictionary8) # Dict 8 won't be clear.

# 12. Copy a Dictionary with the dict() function
# We can also use the constructor dict() to copy a dictionary.
dictionary9 = {"name": "Nguyen", "age": "19", "school": "BVIS"}
dictionary10 = dict(dictionary9)
print(dictionary10)

# 13. Nested Dictionaries
# A dictionary can be nested inside another dictionary. There are two ways to do that.
# 13.1 Create a dictionary with 3 dictionaries inside it:
classmembers = {"Nguyen": {"age": "19", "gender": "Male"}, 
"Scott": {"age": "12", "gender": "Male"},
"Sophie": {"age": "13", "gender": "Female:"}}
print(classmembers)

# 13.2 Create 3 dictionaries, and then create a larger dictionary that contains the three:
Nguyen = {"age": "19", "gender": "Male"}
Scott = {"age": "12", "gender": "Male"}
Sophie = {"age": "13", "gender": "Female:"}
classmembers2 = {"Nguyen": Nguyen, "Scott": Scott, "Sophie": Sophie}
print(classmembers2)

# 14 The dict() constructor
# The dict constructor can be used to create a dictionary from scractch.
new_dictionary = dict(name = "Nguyen", age = 19, school = "BVIS")



