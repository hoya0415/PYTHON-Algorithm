import sys
sys.stdin = open('./10972_input.txt')
from itertools import permutations

N = int(input())
arr = list(range(1,N+1))
check = list(map(int, input().split()))

if sorted(arr, reverse=True) == check:
    print(-1)
else:
    for i in range(N-2, -1, -1):
        if check[i] < check[i+1]:
            a = i
            b = i+1
            break
    for i in range(N-1, -1, -1):
        if check[i] > check[a]:
            l = i
            break
    a_ = check[a]
    check[a] = check[l]
    check[l] = a_

    print(*check[:a+1], *sorted(check[a+1:]))

    # flag = 0
    # for perm in permutations(arr, N):
    #     if flag == 1:
    #         print(*perm)
    #         break
    #     if list(perm) == check:
    #         flag = 1
