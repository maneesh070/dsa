rows = 5

def main():
    for i in range(rows):
        for j in range(i+1):
            if j%2 == 0:
                print((i+1)%2,' ', end='')
            else:
                print((i)%2, ' ', end='')
        print()

if __name__ == '__main__':
    main()