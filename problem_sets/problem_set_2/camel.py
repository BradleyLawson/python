def main():
    cC = input("camelCase: ")
    print(camel_to_snake(cC))

def camel_to_snake(camel_str):
    result = ""
    for ele in camel_str:
        if ele.isupper():
            result += '_' + ele.lower()
        else:
            result += ele
    return f"snake_case: {result}"
    
main()