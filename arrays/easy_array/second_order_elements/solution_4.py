class Solution():
    def getSecondOrderElements(self, arr, n):
        # Merge sort
        self.mergeSort(arr)
        b = []
        b.append(arr[-2])
        b.append(arr[1])
        return b

    def mergeSort(self, arr):
        if len(arr)>1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = 0
            j = 0
            k = 0
            while i<len(L) and j<len(R):
                if L[i]<=R[j]:
                    arr[k] = L[i]
                    i+=1
                    k+=1
                else:
                    arr[k] = R[j]
                    j+=1
                    k+=1
            while i<len(L):
                arr[k] = L[i]
                i+=1
                k+=1
            while j<len(R):
                arr[k] = R[j]
                j+=1
                k+=1


if __name__ == '__main__':
    arr = [2, 4, 1, 7, 8, 3]
    n = len(arr)
    ob = Solution()
    ans = ob.getSecondOrderElements(arr, n)
    print(ans)