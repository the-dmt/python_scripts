def main():

    while True:
        try:
            n1 = int(input("Enter 1st #: "))
        except ValueError:
            print(val_err())
            continue
        op = input("Enter operator: ")
        try:
            n2 = int(input("Enter 2nd #: "))
        except ValueError:
            print(val_err())
            continue

        match op:
            case '+':
                print(add(n1,n2))
            case '-':
                print(subtract(n1,n2))
            case '*':
                print(multiply(n1,n2))
            case '/':
                print(divide(n1,n2))
            case _:
                print('Invalid operator!')
                continue
        break

def add(x,y):
    result = x + y
    return result

def subtract(x,y):
    result = x - y
    return result

def multiply(x,y):
    result = x * y
    return result

def divide(x,y):
    result = x / y
    return result

def val_err():
    msg = 'You must enter an integer!'
    return msg
        

if __name__=="__main__":
    main()
