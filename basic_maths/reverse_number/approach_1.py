
def main():
    n = 345
    x =''
    while n > 1:
        x = x + str(n%10)
        n = n//10
    print(int(x))

if __name__ == '__main__':
    main()