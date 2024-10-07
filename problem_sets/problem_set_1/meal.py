def main():
    whatTime = (input("What time is it? ").strip().lower())
    print(checkTime(convert, whatTime))

# returns user input in decimal
def convert(time):
    h, m = time.split(":")
    convertedTime = int(h) + float(m) / 60
    return convertedTime

# takes the decimal from convert
def checkTime(func, reply):
    if  7.0 <= func(reply) <= 8.0:
        return "breakfast time"
    elif 12.0 <= func(reply) <= 13.0:
        return "lunch time"
    elif 18.0 <= func(reply) <= 19.0:
        return "dinner time"


if __name__ == "__main__":
    main()