def main():
    n = 34148
    reverse = 0
    while n != 0:
        reverse = reverse*10 + n%10
        n = n//10
    print(reverse)

if __name__ == '__main__':
    main()