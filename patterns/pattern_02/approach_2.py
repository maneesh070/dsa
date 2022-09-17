a = 5
def main():
    b = 1
    for i in range(a):
        for j in range(b):
            print('*', end='')
        b += 1
        print('')

if __name__ == '__main__':
    main()
