def main():
    greeting = firstWord(input("Greeting: ").strip().lower())
    print(payout(greeting))

def firstWord(str): 
    return str.split(",")[0]

def payout(saying):
    if saying == "hello":
        return "$0"
    elif saying.startswith("h"):
        return "$20"
    else:
        return "$100"   
    
main()