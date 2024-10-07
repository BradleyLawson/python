# Python Print function documentation
# docs.python.org/3/library/functions.html#print
# Ask user for their name, strip whitespace and capitalize
# first and last name
# input is always string
name = input("What's your name? ").strip().title()

# Remove whitespace from str
# name = name.strip()

# Capitalize user's name
# Will only capitalize first name
# name = name.capitalize()

# Capitalize user's first and last name
# name = name.title()

# Chain together
# name = name.strip().title()

# Split user's name into first name and last name
# this makes use of the name variable
first, last = name.split(" ")

# Say hello to user 
print('hello, ' + name) #this is 1 arg so must provide space

print('hello,', name) #this is 2 args - auto space

# from documentation on print function
# print(*objects, sep=' ', end='\n', dil=sys.stdout, flush=False)
# *objects - print can take any number of objects
# sep=' ' - default seperator is blank space
# end='\n' - default is newline

# override newline
print('hello, ', end='')
print(name)

# override the seperator of single space
print('hello', name, sep='   ')

# Use of quotation marks
print('hello, "friend"')
# Using escape characters
print("hello, \"friend\"")

# format string
print(f'hello, {name}')

print(f'hello, {first}')

# Python string docs
# docs.python.org/3/library/stdtypes.html#string-methods

# creating own function


