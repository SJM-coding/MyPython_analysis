def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num): 
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    return primes
