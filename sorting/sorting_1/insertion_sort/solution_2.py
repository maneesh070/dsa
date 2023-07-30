class Solution():
    def insertion_sort(self, arr, n):
        for i in range(n-1):
            j = 0
            while i-j>=0 and arr[i-j] > arr[i+1-j]:
                arr[i-j], arr[i+1-j] = arr[i+1-j], arr[i-j]
                j += 1
        return arr


if __name__ == '__main__':
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    n = 10
    ob = Solution()
    ans = ob.insertion_sort(arr, n)
    print(ans)