class Solution():
    def topK():
        new_dict = {}
        for i in arr:
            if i in new_dict.keys():
                new_dict[i] = new_dict.get(i) + 1
            else:
                new_dict[i] = 1
        sorted_elements = sorted(new_dict.keys(), key=lambda x: (-new_dict[x], -x))
        return sorted_elements[:k]

if __name__ == '__main__':
    arr = [1, 2, 3, 5, 6, 6, 3, 2, 3]
    n = 8
    k = 2
    ob = Solution
    ans = ob.topK()
    print(ans)


# def get(new_dic, key, key2 = 'ff'):
#     try:
#         return new_dic[key]
#     except:
#         return key2

# new_dic = {1:'121', 2:'dddd'}
# key = 23
# print(get(new_dic, key, key2='ff'))