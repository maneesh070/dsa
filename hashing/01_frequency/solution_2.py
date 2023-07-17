#Frequency of numbers from 1 to n
# array contains integers fom 1 to P

class Solution():
    def fre():
        new_dict = {}
        for i in arr:
            if i in new_dict.keys():
                new_dict[i] += 1
            else:
                new_dict[i] = 1
        for i in range(1, n+1):
            if i in new_dict.keys():
                arr[i-1] = new_dict.get(i)
            else:
                arr[i-1] = 0

        return arr

    def get(self, key, key2=None):
        try:
            return self[key]
        except:
            return key2

if __name__ == '__main__':
    arr = [1,2,3,3,4, 8]
    n = 6
    P = 8
    ob = Solution.fre()
    print(ob)