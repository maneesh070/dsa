height = 5

def main():
    for i in range(height):
        for _ in range(i+1):
            print('*', end='')
        print('')

if __name__ == '__main__':
    main()
