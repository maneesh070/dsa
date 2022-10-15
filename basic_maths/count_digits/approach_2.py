
def main():
    n = 4000
    count = 1
    while n/10 > 1:
        n = n/10
        count += 1
    print(count)


if __name__ == '__main__':
    main()