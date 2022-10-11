lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

def solution(lottos, win_nums):
    l_res = 7
    z_cnt = 0
    for i in range(6):
        if lottos[i] == 0:
            z_cnt += 1
        else:
            try:
                win_nums.pop(win_nums.index(lottos[i]))
                l_res -= 1
            except:
                continue
    answer = []
    if l_res == 7:
        if z_cnt == 0:
            answer = [6, 6]
        else:
            answer = [l_res-z_cnt, 6]
    else:
        answer = [l_res-z_cnt, l_res]
    return answer

print(solution(lottos, win_nums))