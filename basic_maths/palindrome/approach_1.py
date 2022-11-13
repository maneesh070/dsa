def main():
    n = 3432
    x = n
    reverse = 0
    while x != 0:
        reverse = reverse*10 + x%10
        x = x//10
    if n == reverse:
        print(f"The number {n} is a palindrome")
    else:
        print(f"The number {n} is not a palindrome")

if __name__ == '__main__':
    main()