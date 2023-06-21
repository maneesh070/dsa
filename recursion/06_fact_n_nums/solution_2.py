class Solution():
    def factorial_numbers(self):
        global i
        global count
        if i <= n:
            print(i, end=" ")
            count = count + 1
            i = i*count
            self.factorial_numbers()


if __name__ == "__main__":
    n = 24
    i = 1
    count = 1
    ob = Solution()
    ob.factorial_numbers()
    print()
