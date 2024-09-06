def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def dilenia(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is impossible"

def mnojenia(a, b):
    return a * b

def main_menu():
    print("Choose option:")
    print("1. +")
    print("2. -")
    print("3. /")
    print("4. *")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choose = input("You choose (1/2/3/4/5): ")

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choose == '1':
            print(f"{plus(x, y)}")
        elif choose == '2':
            print(f"{minus(x, y)}")
        elif choose == '3':
            print(f"{dilenia(x, y)}")
        elif choose == '4':
            print(f"{mnojenia(x, y)}")
        elif choose == '5':  
            print("Exiting the program.")
            break
        else:
            print("Ancorrect choose")

if __name__ == "__main__":
    main()
