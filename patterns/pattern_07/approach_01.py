height = 10

def main():
    j = 4
    k = 1
    for i in range(5):
        print(j*' ' + k*'*')
        j -= 1
        k +=2

if __name__ == '__main__':
    main()