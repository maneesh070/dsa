class Solution:
    def recursive_bubble_sort(self, arr, n):
        if n == 1:
            return
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        self.recursive_bubble_sort(arr, n-1)


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    n = 5
    ob = Solution()
    ans = ob.recursive_bubble_sort(arr, n)
    print(arr)