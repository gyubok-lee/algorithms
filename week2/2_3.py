def DFS(que,num,depth):
    global local_max
    global arr
    global visited

    if depth == 4:
        if num > local_max :
            local_max = num
        return

    now = que[-1]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]


    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]:
            visited[nx][ny] = 0
            que.append([nx,ny])
            num += arr[nx][ny]
            DFS(que,num,depth+1)

    visited[now[0]][now[1]] = 1
    que.pop()
    num -= arr[now[0]][now[1]]
    return

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

total_max = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 0
        DFS([[i, j]], arr[i][j], 1)
        if total_max < local_max :
            total_max = local_max
print(total_max)