n = 4
def main():
    intchr = 64
    for i in range(1, n+1):
        print(' '*(n-i), end='')
        for j in range(1, i+1):
            print(chr(intchr+j), end='')
        for k in range(i-1, 0, -1):
            print(chr(intchr+k), end='')
        print()

if __name__ == '__main__':
    main()