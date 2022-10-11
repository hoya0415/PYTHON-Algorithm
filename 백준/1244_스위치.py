import sys
sys.stdin = open('1244_input.txt')

def change(num):
    if switch_list[num] == 1:
        switch_list[num] = 0
    elif switch_list[num] == 0:
        switch_list[num] = 1

def switch(g, n):
    if g == 1:
        i = 1
        while i < switch_n + 1:
            if i % n == 0:
                change(i)
            i += 1
    elif g == 2:
        change(n)
        if n > switch_n // 2:
            for i in range(1, switch_n - n + 1):
                if switch_list[n - i] != switch_list[n + i]:
                    break
                elif switch_list[n - i] == switch_list[n + i]:
                    change(n - i)
                    change(n + i)
        else:
            for i in range(1, n):
                if switch_list[n - i] != switch_list[n + i]:
                    break
                elif switch_list[n-i] == switch_list[n+i]:
                    change(n-i)
                    change(n+i)

switch_n = int(input())
switch_list = [0] + list(map(int, input().split()))
students_n = int(input())
students_list = []

for _ in range(students_n):
    gender, number = map(int, input().split())
    students_list.append((gender, number))

while students_list:
    a = students_list.pop(0)
    switch(*a)

for i in range(1, switch_n+1):
    if i % 20 == 0:
        print(switch_list[i])
    else:
        print(switch_list[i], end=' ')

