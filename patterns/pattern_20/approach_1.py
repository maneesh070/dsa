def main():
    n = 4
    for i in range(5):
        print((i+1)*'*'+n*2*' '+(i+1)*'*')
        n -= 1

    for i in range(4, 0, -1):
        print(i*'*'+2*(n+2)*' '+i*'*')
        n += 1


if __name__ == '__main__':
    main()