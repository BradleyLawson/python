def main():
    x, y, z = input("Expression: ").split(" ")
    print(calculate(x, y, z))

def calculate(a, b, c):
    match b:
        case "+":
            return float(a) + float(c)
        case "-":
            return float(a) - float(c)
        case "*":
            return float(a) * float(c)
        case "/":
            return float(a) / float(c)
        
main()