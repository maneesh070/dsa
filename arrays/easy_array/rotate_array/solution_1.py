def rotate_arr(arr, d, n):
        d = d%n
        arr[:] = arr[d:n]+arr[:d]
        return arr

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    n= int(input())
    d = int(input())

    ans = rotate_arr(arr, d, n)
    # print(ans)

    for i in ans:
          print(i, end=" ")
    print()