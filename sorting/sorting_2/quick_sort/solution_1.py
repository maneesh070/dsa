class Solution:
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while i <= j:
            while i<=j and arr[i]<=pivot:
                i += 1
            while arr[j]>pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[low] = arr[low], arr[j]
        return j

    def quick_sort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quick_sort(arr, low, p-1)
            self.quick_sort(arr, p+1, high)


if __name__ == '__main__':
    arr = [4, 5, 2, 7, 6, 1]
    low = 0
    high = len(arr)-1
    ob = Solution()
    ob.quick_sort(arr, low, high)
    print(arr)