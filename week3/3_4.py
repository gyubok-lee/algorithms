# DFS를 활용한 경로탐색 복습

# 최단경로의 길이를 아는 것과 그 경로 자체를 아는것은 다름.
# 모든 경로를 탐색하려면 백트레킹이 필수적

def dfs(x,y,n,track,route):
    dx = (1,-1,0,0)
    dy = (0,0,1,-1)

    if x == n-1 and y == n-1 :
        temp = route[:]
        ans.append(temp)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if check(nx,ny,n,track) :
            track.add((nx,ny))
            route.append([nx,ny])
            dfs(nx,ny,n,track,route)
            track.remove((nx, ny))
            route.pop()
    return

def check(x,y,n,track) :
    global board

    if 0<= x < n and 0<=y<n:
        if(x,y) not in track and board[x][y] == 0:
            return True
    return False

n= int(input())
board = [list(map(int,input().split())) for i in range(n)]
stack = [[0,0]]
track = set([(0,0)])
ans = []
dfs(0,0,n,track,[[0,0]])
for i in ans:
    print(i)
"""
5
0 1 1 1 1
0 0 1 1 1
0 0 1 0 1
0 0 0 0 1
1 1 1 0 0
"""