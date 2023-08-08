def largest_element(arr, n):
    # for i in range(n-1):
    #     if arr[i]>arr[i+1]:
    #         arr[i], arr[i+1] = arr[i+1], arr[i]
    # return arr[-1]
    lar = arr[0]
    for i in range(1, n):
        if arr[i]>lar:
            lar = arr[i]
    return lar


arr = [5, 4, 3, 2, 1]
n = len(arr)
ans = largest_element(arr, n)
print(ans)