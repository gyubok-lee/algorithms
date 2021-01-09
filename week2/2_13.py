# https://www.acmicpc.net/problem/7576

from collections import deque

def BFS(x,y,dep):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cand = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if tomato[nx][ny] == 0:
                cand.append((nx, ny))
    return cand



N, M = map(int,input().split())
tomato = []
rotten = []
cnt = 0

for i in range(M) :
    line = list(map(int,input().split()))
    for j in range(N):
        if line[j] == 1:
            rotten.append((i,j))
        if line[j] == 0:
            cnt +=1
    tomato.append(line)


box = set(rotten)
que = deque([(*i,0)for i in rotten])
depth = 0
while que :
    x,y,depth = que.popleft()
    for next in BFS(x,y,depth) :
        if next not in box :
            que.append((*next,depth+1))
            box.add(next)
if len(box)-len(rotten) != cnt:
    print(-1)
else:
    print(depth)

