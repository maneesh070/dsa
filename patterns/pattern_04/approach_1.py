rep = 6
def main():
    for i in range(1, rep):
        for _ in range(0, i):
            print(i, end='')
        print('')

if __name__ == '__main__':
    main()