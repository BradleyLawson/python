
# INTEGERS - whole numbers
# Ask user for integer input
x = int(input("What's x? "))
y = int(input("What's y? "))


# x = input("What's x? ")
# y = input("What's y? ")

# change to integer
#z = int(x) + int(y)
z = round(x + y)

# print result
# print(z)
# print(x + y)
print(f"{z:,}") #format to add comma if in 1000+

# FLOAT - decimal number
a = float(input("What's a? "))
b = float(input("What's b? "))

# ROUND -  docs.python.org/3/library/functions.html#round
c = round(a + b)
print(c)
# round(number[, ndigits]) 
# square brackets optional

d = float(input("What's d? "))
e = float(input("What's e? "))
f = round(d / e, 2) # rounds to 2 places
print(f)
# print(f"{z:.2f}") prints 2 places 