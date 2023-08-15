# Check if Array Is Sorted and Rotated
class Solution():
    def check_rotated(self, arr, n):
        count = 0
        for i in range(1, n):
            if arr[i-1]>arr[i]:
                count += 1
                if arr[n-1]>arr[0]:
                    count +=1

        if count<=1:
            return 1
        return -1



if __name__ == '__main__':
    arr = [2, 3, 4, 1]
    n = len(arr)
    ob = Solution()
    ans = ob.check_rotated(arr, n)
    print(ans)