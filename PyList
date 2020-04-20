# Python List

# List is a collection which is ordered and changeable. It allows the duplication of members
# Lists belong to the category of a collection (array)

# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
names = ["Nguyen", "Washington", "Adams", "Jefferson", "Madison"]
print(names)

# 1. List Indexing
# Items in a list can be accessed by using their indices, both positively and negatively.
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
print(elements[4]) # Returns Nitrogen
print(elements[-4]) # Returns Lithium

# 2. List Slicing
# Items in a list can also be sliced.
subjects = ["Mathematics", "Physics", "Chemistry"]
print(subjects[0:2]) # Prints Mathematics and Physics
# The first range in the split will be included but the ending range will not be included.
# By leaving out the starting range, the slice will start from the first element
# By leaving out the final range, the slice will start from the start element to the end.
print(subjects[0:]) # Prints all three components
print(subjects[:3]) # Prints all three components
# Negative slicing is also applicable
print(subjects[-2:-1]) # Prints "CPhysics" only as the second range doesn't get included.

# 3. Change Item in List
# Items in a list can be changed.
fruits = ["Banana", "Orange", "Apple"]
fruits[1] = "Dragonfly"
print(fruits)

# 4. for Loop with List
# You can apply a function or a series of algorithm(s) to each and every component of the list with a for loop
animals = ["Dogs", "Cats", "Mice"]
for x in animals:
    x = x + " are cute"
    print(x)

# 5. List item checking
# An item in the list can be checked with the keywords (in) and (not in)
schools = ["BVIS", "AIS", "SSIS", "BIS"]
print ("BVIS" in schools) # Returns True
print ("AMIS" in schools) # Returns False

# 6. The len() function with List
# The len() function can be used to check the length of a list
print(len(schools)) # Returns 4

# 7. Adding Items with append() method
# The append() method will add an item into the list to the end of it.
europiancountries = ["U.K.", "France", "Russia", "Belgium", "Czechoslovakia"]
europiancountries.append("Netherlands") # Add "Netherlands" at the end of the list.
print(europiancountries)

# 8. Adding Items with insert() method
# The insert() method will add an item at a certain index of the list.
europiancountries.insert(0, "Italy") # Add "Italy" at the index 0
print(europiancountries)

# 9. Removing Items with remove() method
# The remove() method removes the exact item that is specified.
races = ["Asian", "Caucasian", "African"]
races.remove("Caucasian")
print(races)

# 10. Removing Items with pop() method
# The pop() method removes the item with a specified index. When the index isn't specified, it removes the last item.
races1 = ["Asian", "Caucasian", "African"]
races1.pop(1)
print(races1)

# 11. The del Keyword
# The del keyword can be used to delete a specified index in a list. It can also be used to delete a whole list.
names1 = ["Nguyen", "Washington", "Adams", "Jefferson", "Madison"]
names2 = ["Nguyen", "Washington", "Adams", "Jefferson", "Madison"]
del names1[2] 
del names2 # name2 is now gone.
print(names1) # "Adams" is deleted from the list names1

# 12. Remove Items with the clear() method
# The clear() method removes every item in the list, but keep the list as an empty list.
elements1 = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
elements1.clear()
print(elements1) # Empty list.

# 13. Copy a list with the copy() method.
# The process of copying a list can't be done with assigning list1 = list2. This creates a reference in list2 on list1 and any changes
# in list1 will eventually being updated in list2. To copy a list, the copy() method is used.
list1 = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
list2 = []
list2 = list1.copy()
list1.clear()
print(list2) # list1 now is empty, however list2 will still have the original content of list1 because it's copied.

# 14. Copy a list with the function list()
# The process of copying the content of a list can be done with the function list()
list3 = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
list4 = []
list4 = list(list3)
list3.clear()
print(list4) # list3 is now empty, however list4 doesn't. Copy complete.

# 15. Join two lists with List Concatenation
# Two lists can be joined with list concatenation.
list5 = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
list6 = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
list7 = list5 + list6
print(list7)

# 16. Join two lists with the extend() method
# Two lists can be joined with the extend() method
list8 = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
list9 = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
list8.extend(list9)
print(list8)

# 17. Join two lists with For Loops
# We can join two list by iterate and append elements of one list into another with a for loop.
list10 = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
list11 = ["Hydrogen", "Helium", "Lithium", "Boron", "Nitrogen", "Carbon"]
for x in list10:
    list11.append(x)
print(list11) # List11 will eventually append every single element in list10.

# 18 The list() constructor
# The list() constructor helps to create new list.
my_list = list((1, 2, 3, "Nguyen", "Strawberry"))
print(my_list)
