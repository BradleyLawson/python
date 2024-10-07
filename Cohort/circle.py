def main():
    number = int(input("What's the radius? "))
    print("The area is", areaOfCircle(number))

def areaOfCircle(radius):
    return 3.14 * radius ** 2

main()