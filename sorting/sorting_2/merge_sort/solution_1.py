class Solution:
    def merge(self, arr, l, m, r):
        # new_arr = [0]*(r-l+1)
        new_arr = []
        i = l
        j = m+1
        k = 0
        while i<= m and j <= r:
            if arr[i] < arr[j]:
                # new_arr[k] = arr[i]
                new_arr.append(arr[i])
                k+=1
                i+=1
            else:
                # new_arr[k] = arr[j]
                new_arr.append(arr[j])
                k+=1
                j+=1
        while i <= m:
            # new_arr[k] = arr[i]
            new_arr.append(arr[i])
            i+=1
            k+=1
        while j <= r:
            # new_arr[k] = arr[j]
            new_arr.append(arr[j])
            k+=1
            j+=1
        i = l
        for ele in new_arr:
            arr[i] = ele
            i += 1

        return arr

    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l+r)//2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid+1, r)
            self.merge(arr, l, mid, r)

if __name__ == '__main__':
    arr = [10, 9, 8, 17, 6, 34, 41, 3, 2, 1]
    n = 10
    l = 0
    r = n-1
    ob = Solution()
    # ans = ob.mergeSort(arr, l , r)
    # print(ans)
    ob.mergeSort(arr, l, r)
    print(arr)