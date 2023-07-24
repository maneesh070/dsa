class Solution:
    def bubbleSort(self, arr, n):
        k = 0
        while k < n:
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            k+=1
        return arr

if __name__ == '__main__':
    arr = [12,3,4,2,55,44]
    n = 6
    ob = Solution()
    ans = ob.bubbleSort(arr, n)
    print(ans)
