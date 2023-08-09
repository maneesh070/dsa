class Solution():
    def getSecondOrderElements(self, arr, n):
        # selection sort
        j = 0

        while j<n-1:
            for i in range(j+1, n):
                if arr[i]<arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
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