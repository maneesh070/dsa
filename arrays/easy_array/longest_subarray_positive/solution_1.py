def longestSubarrayWithSumK(a: [int], k: int) -> int:
    n = len(a)
    count = 0
    max_len = 0
    i = 0
    arr_sum = 0
    for j in range(n):
        arr_sum += a[j]
        count += 1
        if arr_sum == k:
            max_len = max(count, max_len)
        while arr_sum > k:
            arr_sum -= a[i]
            i += 1
            count -= 1
    return max_len

a = [13652, 32990, 36808, 5489, 35236,
     21901, 44849, 16232, 36248, 33222,
     4313, 38171, 8123, 13127, 33084,
     31210, 18121, 16209, 47152, 10226,
     45942, 12170, 31123, 26484, 20619,
     8394, 8985, 26551, 45674, 26632,
     27469, 18905, 20343, 36025, 18686,
     34645, 11871, 16376, 21364, 18070, 26861]

k = 342193
ans = longestSubarrayWithSumK(a, k)
print(ans)