import sys
sys.stdin = open('./2784_input.txt')
from itertools import permutations

arr = [list(input()) for _ in range(6)]
arr.sort()
res = 0
nums = list(range(6))
for num in permutations(nums, 3):
    puz = []
    words = []
    for n in num:
        nums.remove(n)
        puz.append(arr[n])
    for n in nums:
        words.append(arr[n])
    for i in range(3):
        w = []
        for j in range(3):
            w.append(puz[j][i])
        if w in words:
            words.remove(w)
            if not words:
                res = puz
                break
        else:
            nums = list(range(6))
            break
    if res:
        break

if res:
    for r in res:
        print(*r, sep='')
else:
    print(res)
