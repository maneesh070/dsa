class Solution:
    def select(self, arr, i):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        return mini

    def SelectionSort(self, arr, n):
        i = 0
        while i < n-1:
            mini = self.select(arr, i)
            arr[mini], arr[i] = arr[i], arr[mini]
            i += 1

        return arr

if __name__ == '__main__':
    arr = [1, 4, 23, 2, 6]
    n = 5
    ob = Solution()
    ans = ob.SelectionSort(arr, n)
    print(ans)

    # ob = Solution.SelectionSort()
    # print(ob)

# if __name__ == '__main__':
#     n = 4
#     arr = [1, 3, 5, 2]
#     ob = Solution().SelectionSort(arr, n)
#     print(ob)