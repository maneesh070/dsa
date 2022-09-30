num_lines = 4
def main():
    a = ''
    space  = num_lines-1
    for i in range(1, num_lines+1):
        a = a + str(i)
        print(a[0:i], 2*space*' ', a[i::-1])
        space -= 1


if __name__ == '__main__':
    main()