# ==A function that takes input and converts it all to lowercase ==#
def main(): # shows this is the main part of the program
    yell = input() # takes input and stores in variable yell
    print(indoor(yell)) # uses the function indoor and prints result

# ====funtion takes parameter "say" and returns lowercase value===
def indoor(say):
    return say.lower()

main()