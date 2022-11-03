def hcf(A, B):
    x = []
    if A == 0:
        gcd = B
    elif B == 0:
        gcd = A
    elif A != 0 and B != 0:
        if A > B:
            factor = B
            while A%factor != 0 or B%factor != 0:
                factor -= 1
            gcd = factor

        else:
            factor = A
            while B%factor != 0 or A%factor != 0:
                factor -= 1
            gcd = factor

    if A>B:
        M = A
        while M%B != 0 or M%A != 0:
            M += 1
        lcm = M
    else:
        N = B
        while N%A != 0 or N%B != 0:
            N += 1
        lcm = N

    return gcd, lcm


n1 = 24
n2 = 15
gcd = hcf(n1, n2)
print(gcd)