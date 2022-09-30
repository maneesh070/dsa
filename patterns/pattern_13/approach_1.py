num_lines = 5
def main():
    integer = 1
    for i in range(num_lines):
        for j in range(i+1):
            print(integer, ' ', end='')
            integer += 1
        print()

if __name__ == '__main__':
    main()