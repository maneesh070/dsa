def main():
    n = 1534
    num = n
    count = 1
    while num/10 > 1:
        num = num/10
        count += 1
    print(count)

    n = str(n)
    sum_digits = 0
    for i in range(count):
        sum_digits += int(n[i])**count
    print(sum_digits)

    if sum_digits == int(n):
        print(True)
    print(False)


if __name__ == '__main__':
    main()