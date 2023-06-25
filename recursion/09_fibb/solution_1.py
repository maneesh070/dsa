class Solution():
    arr = [1,1]
    def fibb(self, n):
        if len(Solution.arr) >= n:
            return
        Solution.arr.append(Solution.arr[-1]+ Solution.arr[-2])
        self.fibb(n)
        return Solution.arr

if __name__ == "__main__":
    n = 10
    ob = Solution()
    fibb_series = ob.fibb(n)
    print(fibb_series)
