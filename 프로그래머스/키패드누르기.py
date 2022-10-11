def solution(numbers, hand):
    arr = [[8], [2, 4], [1, 3, 5],  [2, 6], [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], [4, 8], [0, 5, 7, 9], [6, 8], [0, 7], [0, 9]]
    l_hand = 10
    r_hand = 11
    answer = ''
            
    def find(d, l, l_res):
        # 목적지랑 출발지가 같으면 바로 종료
        if (d == l):
            return 0
        cnt = 1
        q_arr = [*arr[l]]
        cur_cnt = len(q_arr)
        nxt_cnt = 0
        i = 0
        while len(q_arr) > i:
            c = q_arr[i]
            if cur_cnt <= i:
                cur_cnt += nxt_cnt
                nxt_cnt = 0
                cnt += 1
            if c == d:
                break
            for j in arr[c]:
                if j not in q_arr:
                    if j == d:
                        return cnt + 1
                    q_arr.append(j)
                    nxt_cnt += 1
            i += 1
            if cnt > l_res:
                return 987654321
        return cnt

    for i in range(len(numbers)):
        if numbers[i] % 3 == 0 and numbers[i] > 0:
            answer += 'R'
            r_hand = numbers[i]
            continue
        elif numbers[i] % 3 == 1:
            answer += 'L'
            l_hand = numbers[i]
            continue
        else:
            l_res = find(numbers[i], l_hand, 987654321)
            r_res = find(numbers[i], r_hand, l_res)
            if l_res > r_res:
                answer += 'R'
                r_hand = numbers[i]
            elif l_res < r_res:
                answer += 'L'
                l_hand = numbers[i]
            else:
                if hand == 'left':
                    answer += 'L'
                    l_hand = numbers[i]
                else:
                    answer += 'R'
                    r_hand = numbers[i]
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))