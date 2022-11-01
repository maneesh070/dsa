def hcf(A, B):
    x = []
    if A == 0:
        x.append(B)
    elif B == 0:
        x.append(A)
    elif A != 0 and B != 0:
        if A > B:
            factor = B - 1
            if A%B == 0:
                gcd = B
            else:
                while A%factor != 0 or B%factor != 0:
                    factor -= 1
                gcd = factor

        else:
            factor = A - 1
            if B%A == 0:
                gcd = A
            else:
                while B%factor != 0 or A%factor != 0:
                    factor -= 1
                gcd = factor

        x.append(gcd)

    if A>B:
        if A%B == 0:
            x.append(A)
        else:
            M = A
            while M%B != 0 or M%A != 0:
                M += 1
            x.append(M)
    else:
        if B%A == 0:
            x.append(B)
        else:
            N = B
            while N%A != 0 or N%B != 0:
                N += 1
            x.append(N)

    return x[::]


n1 = 20
n2 = 15
gcd = hcf(n1, n2)
print(gcd)