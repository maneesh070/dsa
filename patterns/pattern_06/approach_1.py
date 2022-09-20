count = 6
def main():
    for i in range(count, 1, -1):
        for j in range(1, i):
            print(j, end='')
        print('')

if __name__ == '__main__':
    main()