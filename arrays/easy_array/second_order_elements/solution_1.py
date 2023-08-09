class Solution():
    def getSecondOrderElements(self, arr, n):
        # Bubble sort
        i = 0
        while i<n-1:
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            i += 1
        b = []
        b.append(arr[-2])
        b.append(arr[1])
        return b



if __name__ == '__main__':
    arr = [2, 4, 1, 7, 8, 3]
    n = len(arr)
    ob = Solution()
    ans = ob.getSecondOrderElements(arr, n)
    print(ans)