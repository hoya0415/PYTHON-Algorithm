import sys
sys.stdin = open('./2839_input.txt')

N = int(input())
res = -1

if N // 5 > 0:
    M = N // 5
    if N % 5 == 0:
        res = M
    else:
        while M >= 0:
            if (N - (5 * M)) % 3 == 0:
                res = M + ((N - (5 * M)) // 3)
                break
            else:
                M -= 1
else:
    if N % 3 == 0:
        res = N // 3

print(res)