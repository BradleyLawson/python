# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1

# a = 0
# while a < 3:
#     print("woof")
#     a += 1

# for _ in [0, 1, 2]:
#     print("meow")

# for _ in range(3):
#     print("woof")

# print("meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()