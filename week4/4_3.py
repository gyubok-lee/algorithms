# https://www.acmicpc.net/problem/7569

from collections import deque

def bfs(q):
    dh = [1,-1]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)): # 해당 큐에 있는 모든 후보군에 대해
            h, x, y = q.popleft()

            for j in range(4): # 같은 박스
                nx, ny = x + dx[j], y + dy[j]
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue
                if tomato[h][nx][ny] == 0:
                    tomato[h][nx][ny] = 1
                    q.append((h, nx, ny))

            for i in range(2): # 위 아래
                nh = h + dh[i]
                if nh >= H or nh < 0:
                    continue
                if tomato[nh][x][y] == 0:
                    tomato[nh][x][y] = 1
                    q.append((nh, x, y))
    if check():
        return cnt - 1
    else:
        return -1

def check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    return False
    return 1

# main
M, N, H = map(int,input().split())
tomato = [[] for _ in range(H)]
que = deque([])

for i in range(H):
    for j in range(N):
        tomato[i].append(list(map(int,input().split())))
        for k in range(M):
            if tomato[i][j][k] == 1:
                que.append((i,j,k))

print(bfs(que))
