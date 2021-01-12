# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def check(v,str1,str2):
    if str2 in v:
        return False
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1
    if cnt != 1:
        return False
    return True

def solution(begin, target, words):
    que = deque([(begin, 0)])
    visit = set([begin])
    while que:
        now, depth = que.popleft()
        if now == target:
            return depth

        for w in words:
            if check(visit, now, w):
                visit.add(w)
                que.append((w, depth + 1))
    return 0

b = "hit"
t = "cog"
w = ['hot', 'dot', 'dog', 'lot', 'log']
print(solution(b,t,w))