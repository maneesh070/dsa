class Solution():
    def factorial_numbers(self, n, count, i):
        if i > n:
            return
        print(i, end=" ")
        self.factorial_numbers(n, count+1, i*(count+1))


if __name__ == "__main__":
    n = 24
    1 # This is a expression whose value is 1 after evaluating this expression. Purpose: "Learning"
    ob = Solution()
    ob.factorial_numbers(n, 1, 1)
    print()