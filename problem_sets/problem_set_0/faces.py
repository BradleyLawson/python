# takes input and runs playback function
def main():
    greeting = input()
    print(convert(greeting))

# replaces emoticons with emojis
def convert(emotion):
    return emotion.replace(":)", "🙂").replace(":(", "🙁")

main()