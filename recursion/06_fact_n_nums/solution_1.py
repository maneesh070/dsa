class Solution():
    def factorial_numbers(self, n, count, i):
        if i > n:
            return
        print(i, end=" ")
        self.factorial_numbers(n, count+1, i*(count+1))


if __name__ == "__main__":
    n = 24
    i = 1
    count = 1
    ob = Solution()
    ob.factorial_numbers(n, count, i)
    print()