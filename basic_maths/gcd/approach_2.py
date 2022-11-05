def lcmhcf(A, B):
    hcf = gcd(A, B)
    lcm = int(hcf*(A/hcf)*(B/hcf))
    return lcm, hcf

def gcd(A, B):
    if A == 0 or B == 0:
        return max(A, B)
    return gcd(max(A, B)%min(A, B), min(A, B))



A = 109
B = 25
LCMnHCF = lcmhcf(A, B)
print(LCMnHCF)