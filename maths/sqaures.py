while True:
    try: 
        num = int(input("Enter #: "))
        squares = tuple(n**2 for n in range(1, num+1))

        if num > 0:
            if num in squares:
                print(f"Yes, {num} is a perfect sqaure!")
            else:
                print(f"Sorry, {num} is NOT a perfect sqaure!")
            break
        elif num < 0:
            print('Negative integers are not allowed!')
        else:
            print('Zero is not allowed!')
    except ValueError:
        print("You must enter an integer!")

