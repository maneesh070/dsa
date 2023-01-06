#Print num from 1 to n using recursion
i = 1
N = 5
def num_print(i, N):
    if i > N:
        return i

    print(i, end=" ")
    return num_print(i+1, N)


series = num_print(i, N)

