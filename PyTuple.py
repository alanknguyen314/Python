# Python Tuple

# Tuple is a collection which is ordered and unchangable. In Python to declare a tuple we use round brackets.
# Lists belong to the category of a collection (array)
# Once a tuple is created, its values can't be changed. The order of the items in the tuple is also fixed.

tuple_name = ("Nguyen", "Harry", "Scott")
print(tuple_name)

# 1. Tuple Indexing
# Items in a tuple can be indexed in the same way with the list(s)
elements = ("Carbon", "Oxygen", "Uranium")
print(elements[1]) # Prints "Oxygen"
print(elements[-1]) # Prints "Uranium"

# 2. Tuple Slicing
# Tuples can be sliced just like with lists.
elements1 = ("Carbon", "Oxygen", "Uranium")
print(elements[0:2]) # Last one is exclusive, so "Uranium" didn't get printed.
print(elements[-3:-1]) # Last one is exclusive, so "Uranium" didn't get printed.

# 3. How to change Tuple values
# In order to change values of a tuple, we can change the tuple into a list and then change the its items. Then, we change
# the list back into a tuple.
names = ("Washington", "Nguyen", "John", "Quincy", "Adams")
names_list = list(names)
names_list.insert(1, "Jefferson")
names = tuple(names_list)
print(names) # Tuple now got a new value: "Jefferson" at position 1

# 4. for Loop with Tuple
# You can iterate through a tuple the same way with a list using a for loop
animals = ("Cats", "Dogs", "Dinosaurs")
for x in animals:
    print("I love", x)

# 5. The len() function with Tuples
# We can apply the len() function to tuples to find their length
subjects = ("Mathematics", "Science", 'Literature')
print(len(subjects))

# 6. Tuples with only one item
# When creating tuples with only one item, a comma is required after the tuple so that it the program
# recognizes it as a tuple. Else, it's going to be a string, or a number, or the type of whatever that
# is in the "tuple"
new_tuple = ("Nguyen", ) # Tuple
new_tuple1 = ("Nguyen") # String
print(new_tuple, new_tuple1)

# 7. The del keyword with Tuples
# The del keyword can be used to permanently delete a tuple
new_tuple2 = ("Mathematics", "Science", 'Literature')
del new_tuple2 # new_tuple2 is now gone

# 8. Join two tuples with Tuple Concatenation
# Tuples can be joined with a "+" symbol
tuple1 = ("Mathematics", "Science", 'Literature')
tuple2 = ("Mathematics", "Science", 'Literature')
tuple3 = tuple1 + tuple2 
print(tuple3)

# 9. The tuple() constructor
# Tuple can be created with the tuple() constructor
newest_tuple = tuple(("Ryan", "Harry", "William"))
print(newest_tuple)








