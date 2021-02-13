# https://www.acmicpc.net/problem/5014

from collections import deque

def BFS(q,f,u,d) :
    while q:
        now, cnt = q.popleft()
        if now == G:
            return cnt
        if (now + u <= f) and now + u not in visit :
            visit.add(now+u)
            q.append((now+u,cnt+1))
        if (now - d >= 1) and now - d not in visit :
            visit.add(now-d)
            q.append((now-d,cnt+1))
    return "use the stairs"

F, S, G, U, D = map(int,input().split())

visit = set([S])
que = deque([(S,0)])
print(BFS(que,F,U,D))
