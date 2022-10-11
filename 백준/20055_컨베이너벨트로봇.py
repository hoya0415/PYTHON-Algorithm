import sys
sys.stdin = open('./20055_input.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))
s = cnt = 0
e = N-1
robot = [0] * (2 * N)

while arr.count(0) < K:
    cnt += 1
    if robot[e]:
        robot[e] = 0
    s = (s - 1) % (2 * N)
    e = (e - 1) % (2 * N)
    for i in range(e, e-N, -1):
        if robot[i]:
            if i == e:
                robot[e] = 0
            else:
                next = (i+1) % (2 * N)
                if robot[next] == 0 and arr[next] > 0:
                    robot[i] = 0
                    robot[next] = 1
                    arr[next] -= 1
        if (i % (2 * N)) == s and arr[s] > 0:
            robot[i] = 1
            arr[s] -= 1

print(cnt)