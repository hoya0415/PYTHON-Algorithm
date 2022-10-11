import sys
sys.stdin = open('16199_input.txt')


BY, BM, BD = map(int, input().split())
Y, M, D = map(int, input().split())

man = 0
korean = 0
year = 0

if Y > BY:
    if M > BM:
        man = Y - BY
    elif M == BM:
        if D >= BD:
            man = Y - BY
        else:
            man = Y - BY - 1
    else:
        man = Y - BY - 1
    korean = Y - BY + 1
    year = Y - BY
else:
    man = 0
    korean = 1
    year = 0

print(man)
print(korean)
print(year)


