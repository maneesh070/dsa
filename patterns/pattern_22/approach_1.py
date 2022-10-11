n = 4
def main():
    for i in range(1-n, n):
        for j in range(1-n, n):
            if abs(i) > abs(j):
                print(abs(i)+1, end='')
            else:
                print(abs(j)+1, end='')
        print()

if __name__ == '__main__':
    main()