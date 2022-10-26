def hcf(A, B):
    if A == 0:
        return B
    elif B == 0:
        return A
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


        return gcd



n1 = 0
n2 = 15
gcd = hcf(n1, n2)
print(gcd)