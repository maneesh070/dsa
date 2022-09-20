reach = 5
def main():
    for i in range(5, 0, -1):
        for j in range(i):
            print('*', end='')
        print('')

if __name__ == '__main__':
    main()