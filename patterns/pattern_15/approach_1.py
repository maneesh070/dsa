def main():
    for i in range(5):
        for j in range(65, 70-i):
            print(chr(j), end='')
        print()

if __name__ == '__main__':
    main()