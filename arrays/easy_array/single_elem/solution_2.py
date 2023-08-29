class Solution():
    def get_single_element(self, arr, n):
        new_dict = {}
        for i in arr:
            if i in new_dict.keys():
                new_dict[i] += 1
            else:
                new_dict[i] = 1
        for i in new_dict:
            if new_dict[i] == 1:
                return i


if __name__ == '__main__':
    arr = [1,1,2,2, 3]
    n = len(arr)
    ob = Solution()
    ans = ob.get_single_element(arr, n)
    print(ans)