#Sum of all divisior of all integers up to a given number
n = 4
def main():
    sum_int = 0
    for i in range(1, n+1):
        j = 1
        while j<= i:
            if i%j == 0:
                sum_int += j
            j += 1
    print(sum_int)


if __name__ == '__main__':
    main()