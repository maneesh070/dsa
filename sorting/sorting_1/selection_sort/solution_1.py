class Solution():
    def selection_sort():
        j = 0
        steps = 0
        while j < n-1:
            for i in range(j+1, n):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                steps+= 1
            j += 1
        print(steps)
        return arr

if __name__ == '__main__':
    n = 10
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ob = Solution.selection_sort()
    print(ob)