def main():
    response = input("What is the Great Question of Life, the Universe and Everything? ").strip().lower()
    print(isMeaning(response))

def isMeaning(input):
    match input:
        case "42" | "forty-two" | "forty two":
            return "yes"
        case _:
            return "no"

main()