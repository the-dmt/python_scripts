def main():
    print(is_prime(6))
    print(is_prime(3))
    print(generate_primes(100))

def generate_primes(n: int) -> list:

    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    
    return primes

def is_prime(n: int) -> bool:

    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


if __name__ == "__main__":
    main()
