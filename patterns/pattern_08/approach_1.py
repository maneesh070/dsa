def main():
    lines = 0
    stars = 9
    for i in range(5):
        print(lines*' '+stars*'*')
        lines += 1
        stars -= 2

if __name__ == '__main__':
    main()