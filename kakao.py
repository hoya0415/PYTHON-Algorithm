import sys
sys.stdin = open('kakao_input.txt')

def solution(id_list, report, k):
    cnt_list = [0] * len(id_list)
    declare = []
    answer = [0] * len(id_list)

    for i in report:
        for j in range(len(id_list)):
            if i in id_list[j]:
                cnt_list[j] += 1

    for r in range(len(cnt_list)):
        if cnt_list[r] >= 2:
            declare.append(id_list[r])

    for c in range(len(report)):
        for z in range(len(declare)):
            if declare[z] in report[c]:
                answer[c] += 1

    return answer

id_list = input()
report = input()
k = int(input())

print(solution(id_list, report, k))
