#Printing pattern n times using recursion
n = 5

def print_ptrn(n):
    if n == 0:
        return
    print_ptrn(n-1)
    print("GFG", end=" ")

pattern = print_ptrn(n)
# print(pattern)