class Solution():
    def getSecondOrderElements(self, arr, n):
        # quick sort
        low = 0
        high = n-1
        self.quickSort(arr, low, high)
        b = []
        b.append(arr[-2])
        b.append(arr[1])
        return b
    def partition(self,arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while i<=j:
            while i<=j and arr[i]<=pivot:
                i += 1
            while arr[j]>pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[low] = arr[low], arr[j]
        return j

    def quickSort(self, arr, low, high):
        if low<high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p-1)
            self.quickSort(arr, p+1, high)


if __name__ == '__main__':
    arr = [2, 4, 1, 7, 8, 3]
    n = len(arr)
    ob = Solution()
    ans = ob.getSecondOrderElements(arr, n)
    print(ans)