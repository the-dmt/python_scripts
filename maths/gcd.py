def main():
    a = int(input("Enter 1st #: "))
    b = int(input("Enter 2nd #: "))
    c = int(input("Enter 3rd #: "))

    print("*" * 10)

    if a < b and a < c:
        if b < c:
            calculateGCD(a,b,c)
        else: 
            calculateGCD(a,c,b)
    elif b < a and b < c:
        if a < c:
            calculateGCD(b,a,c)
        else:
            calculateGCD(b,c,a)
    else:
        if a < b:
            calculateGCD(c,a,b)
        else:
            calculateGCD(c,b,a)

    print("*" * 10)


def calculateGCD(low: int, middle: int, high: int):

    gcd = 0

    if high % low != middle % low:
        gcd = 1
    elif middle % low == 0:
        gcd = low
    else:
        gcd = middle % low

    print(f"The gcd is {gcd}")

if __name__ == "__main__":
    main()
