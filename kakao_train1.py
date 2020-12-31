from collections import defaultdict
from bisect import bisect_left, bisect_right
# https://programmers.co.kr/learn/courses/30/lessons/60060
# ?가 있는 구간을 빠르게 찾는 것이 중요: 너무 어려웠음. trie알고리즘
# bisect는 정렬된 리스트에서 입력값이 위치할 인덱스를 반환.
def count_by_range(lst, start, end):
    return bisect_right(lst, end) - bisect_left(lst, start)

def solution(words, queries):
    answer = []
    cands = defaultdict(list)
    reverse_cands = defaultdict(list)
    # 길이별 저장
    for word in words:
        cands[len(word)].append(word) # 단어 길이에 따른 딕셔너리 생성
        reverse_cands[len(word)].append(word[::-1]) # 단어 길이에 따른 역순 단어 딕셔너리 생성
    # 정렬 O(NlogN)
    for cand in cands.values():
        cand.sort()
    for cand in reverse_cands.values():
        cand.sort()
    print(cands)
    # 탐색 O(N * logM)
    for query in queries:
        if query[0] == '?': # 와일드카드 접두사 일 때
            lst = reverse_cands[len(query)]
            start, end = query[::-1].replace('?','a'), query[::-1].replace('?','z')
        else: # 와일드카드 접미사 일 때
            lst = cands[len(query)]
            start, end = query.replace('?','a'), query.replace('?','z')
        answer.append(count_by_range(lst, start, end))
    return answer

w = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q = ["fro??", "????o", "fr???", "fro???", "pro?","?????"]
print(solution(w,q))