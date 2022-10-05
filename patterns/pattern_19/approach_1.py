def main():
    n = 2
    m = 4
    for i in range(5):
        if i == 0:
            print(10*'*')
        else:
            print(m*'*'+(n*' ')+m*'*')
            m -= 1
            n += 2
    m = 1
    n = 4
    for j in range(5):
        print(m*'*'+2*n*' '+m*'*')
        m += 1
        n -= 1


if __name__ == '__main__':
    main()