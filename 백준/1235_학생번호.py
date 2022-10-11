import sys
sys.stdin = open('./1235_input.txt')

N = int(input())
stus = []
res = 0

for _ in range(N):
    stus.append(input())

for i in range(1, len(stus[0])+1):
    nums = []
    for j in range(N):
        if stus[j][-i:] not in nums:
            if j == N-1:
                res = i
                break
            nums.append(stus[j][-i:])
        else:
            break
    if res == i:
        break

print(res)