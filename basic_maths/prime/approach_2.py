def isPrime(n):
    is_prime = True
    if n == 1 or n == 2:
        return is_prime

    root = sqrt(n)
    for i in range(2, root + 1):
        if n%i == 0:
            is_prime = False
            return is_prime

    return is_prime

def isItPrime(n):
    if n == 1 or n == 2:
        return True

    root = sqrt(n)
    for i in range(2, root + 1):
        if n%i == 0:
            return False
    return True

def sqrt(num):
    step = 0.1
    root = 1
    while True:
        if root*root <= num + step and root*root >= num - step:
            print(f"Value of start is: {root}")
            return round(root, 3)

        root += step


n = 25
ans = isPrime(n)
print(ans)