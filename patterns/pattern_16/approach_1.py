last_alpha = 70
def main():
    for i in range(65, last_alpha):
        for j in range(0, i-64):
            print(chr(i), end='')
        print()

if __name__ == '__main__':
    main()