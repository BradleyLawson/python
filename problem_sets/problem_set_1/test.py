# def lastWord(str):
#     # if  "." not in str:
#     #     print (str)
#     # else:
#         print (str.split(".")[-1])
#         print (str.split(".", 1))
# lastWord("happy.txt.pdf.doc")

# x, y, z = input("Expression: ").split(" ")

# print(x, y, z)

# print (float(x), y, float(z))

# def convert(time):
#     h, m = time.split(":")
#     hours = int(h)
#     minutes = float(m) / 60
#     decimalTime = int(h) * 3600 + int(m) * 60
#     print (hours)
#     print (minutes)
#     print(hours + minutes)
#     print (9 - (hours + minutes))
# convert("7:30")

# def convert(time):
#     h, m = time.split(":")
#     convertedTime = int(h) + float(m) / 60

#     if  7.0 <= convertedTime <= 8.0:
#         print ("breakfast time")
#     elif 12.0 <= convertedTime <= 13.0:
#         print ("lunch time")
#     elif 18.0 <= convertedTime <= 19.0:
#         print ("dinner time")

# convert("6:30")

def convert(time):
    h, m = time.split(":")
    convertedTime = int(h) + float(m) / 60
    print (convertedTime)

def checkTime(reply):
    if  7.0 <= reply <= 8.0:
        print ("breakfast time")
    elif 12.0 <= reply <= 13.0:
        print ("lunch time")
    elif 18.0 <= reply <= 19.0:
        print ("dinner time")

convert("6:30")
checkTime("7:30")