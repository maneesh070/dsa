class Solution():
# Frequency of nos. using loop

    def frequency_count(self):
        a = []
        arr.sort()
        for i in range(1, P+1):
            count = 0
            for j in range(0, n):
                if i == arr[j]:
                    count += 1

            a.append(count)
        return a


if __name__ == '__main__':
    arr = [2, 3, 2, 3, 6, 1, 4, 5]
    n = 8
    P = 6
    ob = Solution()
    frequency = ob.frequency_count()
    print(frequency)