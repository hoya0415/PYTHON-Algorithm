import sys
sys.stdin = open('./2231_input.txt')

N = int(input())
res = 0

for i in range(1, N):
    str_list = [i] # 본인, 본인의 분해를 담을 리스트
    # 문자열로 자릿수 분해해서 정수로 바꿔 리스트에 담는다
    i = str(i)
    for j in i:
       str_list.append(int(j))
    # 리스트의 합과 분해합이 같으면 생성자로 인정
    if sum(str_list) == N:
        res = i
        break

print(res)