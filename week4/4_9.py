# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations

def solution(orders, course):
    course_comb = dict() # 개수별 모든 조합
    orders_cand = [] # 각 주문마다의 모든 조합

    # 자료구조 셋팅
    for i in course:
        course_comb[i] = []
    for o in orders :
        cand = []
        o = list(sorted(o))
        for i in course :
            if len(o) >= i :
                c = list(combinations(o,i))
                course_comb[i] += c
                cand.append(c)
            else :
                cand.append([])
        orders_cand.append(cand)

    # 각 코스별 최고 인기 조합 찾기
    res = []
    for i in range(len(course)) :
        max_cnt = 0
        tmp = []
        for j in set(course_comb[course[i]]) :
            cnt = 0
            for k in orders_cand :
                if j in k[i] :
                    cnt += 1
            if cnt > max_cnt and cnt > 1:
                tmp = [j]
                max_cnt = cnt
            elif cnt == max_cnt and cnt > 1:
                tmp.append(j)
                max_cnt = cnt

        for _ in tmp :
            res.append(''.join(_))
    res.sort()
    return res

ord = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
cse = [2,3,5]
print(solution(ord,cse))