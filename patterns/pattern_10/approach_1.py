def main():
    for i in range(5):
        for _ in range(i + 1):
            print('*', end='')
        print()
    for j in range(4, 0, -1):
        for _ in range(j):
            print('*', end='')
        print()

if __name__ == '__main__':
    main()