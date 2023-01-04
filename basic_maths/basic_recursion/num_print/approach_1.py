#Print num from 1 to n using recursion
n = 1
N = 5
def num_print(n, N):
    if N > 1:
        print(n, end=" ")
        return num_print(n+1, N-1)
    else:
        return n

series = num_print(n, N)
print(series)

