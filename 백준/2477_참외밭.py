import sys
sys.stdin = open('2477_input.txt')

C = int(input())
d = []
w = []
b1 = 0
b2 = 0
s1 = 0
s2 = 0

for i in range(6):
    a, b = map(int, input().split())
    d.append(a)
    w.append(b)

for j in range(6):
    if d.count(d[j]) == 1:
        if b1 == 0:
            b1 = w[j]
        else:
            b2 = w[j]

for z in range(6):
    if d.count(d[z]) == 2:
        if w[z-1] != b1 and w[(z+1)%6] != b1 and w[z-1] != b2 and w[(z+1)%6] != b2:
            if s1 == 0:
                s1 = w[z]
            else:
                s2 = w[z]

print((b1*b2 - s1*s2 )*C)