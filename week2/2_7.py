# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    rows = len(relation)
    cols = len(relation[0])

    # 모든 조합 찾기
    candidates = []
    for i in range(1, cols + 1):
        candidates.extend(combinations(range(cols), i))

    # 고유키 찾기
    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == rows:
            final.append(keys)

    # 후보키 찾기
    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)



rere= [["100","ryan","music","2"],["200","apeach","math","2"],
       ["300","tube","computer","3"],["400","con","computer","4"],
       ["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(rere))

