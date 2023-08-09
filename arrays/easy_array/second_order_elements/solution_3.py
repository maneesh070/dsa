class Solution():
    def getSecondOrderElements(self, arr, n):
        # Insertion sort
        for i in range(n-1):
            j = 0
            while i-j>=0:
                if arr[i-j]>arr[i-j+1]:
                    arr[i-j], arr[i+1-j] = arr[i+1-j], arr[i-j]
                j += 1

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