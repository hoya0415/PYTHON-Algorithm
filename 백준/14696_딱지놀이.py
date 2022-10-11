import sys
sys.stdin = open('14696_input.txt')

round_n = int(input())

for _ in range(round_n):
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_n = a_list.pop(0)
    b_n = b_list.pop(0)
    ans = 'D'

    for i in range(4, 0, -1):
        a = a_list.count(i)
        b = b_list.count(i)
        if a != b:
            if a > b:
                ans = 'A'
                break
            else:
                ans = 'B'
                break

    print(ans)