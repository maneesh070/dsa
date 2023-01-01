n = 10
def main():
    a = []
    if n == 1 or n == 2:
        print('Prime')
    else:
        for i in range(2, n):
            if n%i == 0:
                a.append(i)
    if len(a) == 0:
        print("Prime")

    print("Non-Prime")

if __name__ == '__main__':
    main()