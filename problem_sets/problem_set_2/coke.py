def main():
    total_due = 50
    print(f"Amount Due: {total_due}" )
    amount_still_owed(total_due)


def amount_still_owed(d):
    
    remaining = int(input("Insert Coin: "))
    return d - remaining



main()