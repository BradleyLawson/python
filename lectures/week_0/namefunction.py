# Create own hello function
# Allows you to define function below the code
def main(): # shows this is the main part of the program
    name = input("what's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
