def main():
    spaces = 4
    stars = 1
    for i in range(5):
        print(spaces*' ' + stars*'*')
        spaces -= 1
        stars += 2
    stars -= 2
    spaces += 1
    for j in range(5):
        print(spaces*' ' + stars*'*')
        spaces += 1
        stars -= 2

if __name__ == '__main__':
    main()