def hcf(A, B):
    x = []
    if A == 0:
        gcd = B
    elif B == 0:
        gcd = A
    elif A != 0 and B != 0:
        factor = min(A, B)
        while A%factor != 0 or B%factor != 0:
            factor -= 1
        gcd = factor

    M = max(A, B)
    while M%B != 0 or M%A != 0:
        M += 1
    lcm = M

    return gcd, lcm


n1 = 24
n2 = 15
gcd = hcf(n1, n2)
print(gcd)