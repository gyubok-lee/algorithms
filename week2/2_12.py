# https://www.acmicpc.net/problem/2178

# BFS는 각 정점을 최단경로로 방문한다.
from collections import deque
def BFS(x,y,dep) :
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cand = []
    for i in range(4):
        nx, ny = x +dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M :
            if board[nx][ny] == 1:
                cand.append((nx,ny))
    return cand


N, M = map(int,input().split())
board = [[int(j) for j in input()] for k in range(N)]
route = set([(0,0)])
que = deque([(0,0,1)])

while que :
    x,y,depth = que.popleft()
    if x == N-1 and y == M-1:
        print(depth)
        break
    for next in BFS(x,y,depth) :
        if next not in route :
            que.append((*next,depth+1))
            route.add(next)


