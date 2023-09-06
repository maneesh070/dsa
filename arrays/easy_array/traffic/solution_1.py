class Solution():
    def traffic(self, n, m, vehicle):
        ws = n
        while ws > 0:
            for j in range(0, n-ws+1):
                temp_sum = sum(vehicle[j:j+ws]) + m
                if temp_sum >= ws:
                    return ws
            ws -= 1
        return temp_sum


if __name__ == '__main__':
    vehicle = [0, 0, 1, 1, 0, 1,0, 0, 0, 1, 1, 1, 1, 1, 1]
    n = len(vehicle)
    m = 2
    ob = Solution()
    ans = ob.traffic(n, m, vehicle)
    print(ans)