class Solution():
    def moveZeros(self, arr, n):
        j = 0
        for i in range(n):
            if arr[i] != 0:
                arr[j] = arr[i]
                j += 1
        while j<n:
            arr[j] = 0
            j += 1
        return arr

if __name__ == '__main__':
    arr = [1, 5, 6, 0, 4, 0, 2]
    n = len(arr)
    ob = Solution()
    ans = ob.moveZeros(arr, n)
    print(ans)