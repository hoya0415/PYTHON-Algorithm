import sys
sys.stdin = open('./2805_input.txt')

N, M = map(int, input().split())

t_arr = list(map(int, input().split()))
max_h = res = max(t_arr)
t_arr.sort(reverse=True)
cnt = 0
for i in range(max_h-1, -1, -1):
    for j in range(N):
        if t_arr[j] - i > 0:
          cnt += 1
          t_arr[j] -= 1
          if cnt >= M:
              res = i
              break
        else:
            break
    if res == i:
        break

print(res)