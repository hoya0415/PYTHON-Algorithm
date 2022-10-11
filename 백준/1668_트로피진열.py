import sys
sys.stdin = open('1668_input.txt')

N = int(input())
arr = []
l_v = 1
r_v = 1


for i in range(N):
    arr.append(int(input()))

h = arr[0]
for j in range(1, N):
    if arr[j] > arr[j-1] and h < arr[j]:
        l_v += 1
        h = arr[j]

h = arr[-1]

for z in range(N-2, -1, -1):
    if arr[z] > arr[z+1] and h < arr[z]:
        r_v += 1
        h = arr[z]

print(l_v)
print(r_v)