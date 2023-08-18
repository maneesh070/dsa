class Solution():
    def missing_num(self, arr, n):
        # Any sorting method to sort the array
        #Insertion sort
        for i in range(n-1):
            j = 0
            while i-j>=0:
                if arr[i-j]>arr[i-j+1]:
                    arr[i-j], arr[i-j+1] = arr[i-j+1], arr[i-j]
                j += 1
        for i in range(n):
            if arr[i] != i:
                return i
            elif arr[i] == i and arr[-1] != n:
                return n


if __name__ == '__main__':
    arr = [1, 5, 6, 0, 2, 4,7, 3]
    n = len(arr)
    ob = Solution()
    ans = ob.missing_num(arr, n)
    print(ans)