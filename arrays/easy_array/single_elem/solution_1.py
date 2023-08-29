class Solution():
    def get_single_element(self, arr, n):
        if n ==1:
            return arr[0]
        else:
            for i in range(0,n-1,2):
                if arr[i] != arr[i+1]:
                    return arr[i]
            if arr[-1] != arr[-2]:
                return arr[-1]

if __name__ == '__main__':
    arr = [1,1,2,2, 3]
    n = len(arr)
    ob = Solution()
    ans = ob.get_single_element(arr, n)
    print(ans)