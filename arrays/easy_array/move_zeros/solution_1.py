class Solution():
    def moveZeros(self, arr, n):
        r = n
        for i in range(n):
            if arr[i]==0:
                arr.append(0)
        j = 0
        for k in range(r-j):
            if arr[k-j] == 0:
                arr.remove(arr[k-j])
                j += 1
        return arr



if __name__ == '__main__':
    arr = [1, 4, 6, 0, 4, 0, 1]
    n = len(arr)
    ob = Solution()
    ans = ob.moveZeros(arr, n)
    print(ans)