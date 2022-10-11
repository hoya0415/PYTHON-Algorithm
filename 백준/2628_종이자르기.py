import sys
sys.stdin = open('2628_input.txt')

w, h = map(int, input().split())
n = int(input())
w_list = [0]
h_list = [0]
max_a = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        h_list.append(b)
    elif a == 1:
        w_list.append(b)

w_list.append(w)
h_list.append(h)
w_list.sort()
h_list.sort()

for i in range(1, len(w_list)):
    for j in range(1, len(h_list)):
        area = (w_list[i] - w_list[i-1]) * (h_list[j] - h_list[j-1])
        if area > max_a:
            max_a = area

print(max_a)