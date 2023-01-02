def isPrime(n):
    is_prime = True
    if n == 1 or n == 2:
        return 'Prime'
    else:
        for i in range(2, n):
            if n%i == 0:
                is_prime = False

    if is_prime == True:
        return 'Prime'
    return 'Non-Prime'

n = 29
ans = isPrime(n)
print(ans)