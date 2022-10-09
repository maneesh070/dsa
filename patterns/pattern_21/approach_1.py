n = 4
def main():
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(n):
                print('*', end='')
            print()
        else:
            print('*'+(n-2)*' '+'*')

if __name__ == '__main__':
    main()