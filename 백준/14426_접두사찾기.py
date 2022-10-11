import sys
sys.stdin = open('./14426_input.txt')

N, M = map(int, input().split())
S = list(input() for _ in range(N))
cnt = 0

for i in range(M):
    c = input()
    for s in S:
        if c[0] == s[0]:
            if c in s:
                cnt += 1
                break

print(cnt)
