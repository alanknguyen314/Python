# Python Boolean 
# bool

# In programming you often need to know if an expression is True or False. 
# You can evaluate any expression in Python, and get one of two answers, True or False.
print(5==5) # Returns True
print(15==4) # Returns False

# 1. When an if statement is executed, the condition for that statement must be true. If the statement
# turns out to be false, the elif statements will be checked. If none of the statements is true, the commands
# after "else:" is executed
number = 5
if number == 3:
    print("The number is 3") # False
elif number == 2:
    print("The number is 2") # False
else:
    print("The number isn't 2 or 3") # Returns this statement since the number is 5.

# 2. The bool() function
# The bool() function allows you to evaluate any value, and give you True or False in return.
# With the bool() function, most of the passed values are true. There are some rules to this.
# - Any string is True, except empty strings ("")
# - Any number is True, except the number (0)
# - Any list, tuple, set and dictionary are True, except empty ones. Example: [], (), {}.
# - The value None or False will always return False.
# - Another value that will eventually return to False is an object that is made from a class that contains a __len__ function()
#   that returns 0 or False

print(bool(0))
print(bool(False))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(""))

class new_class():
    def __len__(self):
        return 0

my_object = new_class()
print(bool(my_object))


