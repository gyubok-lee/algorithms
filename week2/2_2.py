# https://www.acmicpc.net/problem/14500

# 백트레킹 기초 탄탄히 할 것. 완전탐색 + 재귀 + 메모이제이션
def finder(depth,x,y,res):
    global total_max
    global stack

    res += arr[x][y]
    if depth == 4:
        total_max = max(res,total_max)
        return

    stack.append([x,y])
    visited[x][y] = 1

    for _ in stack:
        for i,j in [ (-1,0), (1,0), (0,-1), (0,1) ]:
            nx = _[0] + i
            ny = _[1] + j
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                finder(depth+1, nx,ny,res)

    stack.pop()
    visited[x][y] = 0
    return

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

total_max = 0
stack = []
visited = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        result = 0
        finder(1,i,j,0)
print(total_max)