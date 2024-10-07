# takes input and runs playback function
def main():
    statement = input()
    print(playback(statement))

# replaces space with ...
def playback(fasttalk):
    return fasttalk.replace(" ", "...")

main()