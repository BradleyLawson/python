def main():
    mass = int(input("m: "))
    print("E: ", joules(mass))

def joules(kilos):
    return kilos * 300000000**2

main()