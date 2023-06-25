class Solution():
    def fibb(self, n):
        if n <= 2:
            return 1
        return self.fibb(n-1) + self.fibb(n-2)

if __name__ == "__main__":
    n = 10
    ob = Solution()
    fibb_num = ob.fibb(n)
    print(fibb_num)