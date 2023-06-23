class Solution:
    arr = []
    def factorialNumbers(self, N):
        self.fact_num(N, 1, 1)
        return Solution.arr

    def fact_num(self, n, i, count):
        if i > n:
            return None
        Solution.arr.append(i)
        self.fact_num(n, i*(count+1), count+1)

if __name__ == "__main__":
    n = 2
    ob = Solution()
    ans = ob.factorialNumbers(n)
    print(ans)


