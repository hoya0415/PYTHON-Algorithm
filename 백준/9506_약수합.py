import sys
sys.stdin = open('./9506_input.txt')

while True:
    n = int(input())
    if n == -1:
        break

    yak = []

    for i in range(2, n):
        if n % i == 0:
            yak.append(i)

    if sum(yak) + 1 == n:
        print(n, '= 1', end='')
        for y in yak:
            if yak.index(y) == len(yak) -1:
                print(' +', y)
            else:
                print(' +', y, end='')
    else:
        print(n, 'is NOT perfect.')
