class Solution():
    new_arr = []
    def rev_array(self, arr):
        if len(arr) == 0:
            return
        b = arr.pop(-1)
        Solution.new_arr.append(b)
        self.rev_array(arr)
        return Solution.new_arr


if __name__ == '__main__':
    arr = [1, 3, 5, 6]
    ob = Solution()
    array = ob.rev_array(arr)
    print(array)