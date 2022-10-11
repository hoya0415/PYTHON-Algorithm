import sys
sys.stdin = open('./9934_input.txt')

N = int(input())
In = list(map(int, input().split()))
L = 2**(N) - 1
arr = [[] for _ in range(N)]
d = 0
for i in range(1, N+1):
    for j in range(L):
        if j % 2**(i) - d == 0:
            arr[N-i].append(In[j])
    d += 2**(i-1)

for a in arr:
    print(*a)