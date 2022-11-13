#list of divisors of a given number
n = 34
def main():
    divi_set = []
    for i in range(1, n+1):
        if n%i == 0:
            divi_set.append(i)
    print(divi_set[::])

if __name__ == '__main__':
    main()