num_lines = 5
def main():
    for i in range(num_lines):
        for j in range(65,65+i+1):
            print(chr(j), end='')
        print()

if __name__ == '__main__':
    main()