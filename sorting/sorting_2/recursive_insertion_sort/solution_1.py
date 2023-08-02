class Solution:
    def recursion_insertion_sort(self, arr, n):
        if n == 1:
            return
        j = 0
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        self.recursion_insertion_sort(arr, n-1)

if __name__ == '__main__':
    arr = [2, 4, 1, 8, 5]
    n = 5
    ob = Solution()
    ans = ob.recursion_insertion_sort(arr, n)
    print(arr)