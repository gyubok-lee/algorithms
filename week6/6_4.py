def dfs(x,y,visit,n) :
    if x == n-1 and y == n-1 :
        route.append([i for i in visit])
        return
    deltas =  [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for d in deltas :
        nx, ny = x+d[0], y+ d[1]
        if 0<=nx<n and 0<=ny<n :
            if (nx,ny) not in visit and m[ny][nx] == 0:
                visit.append((nx,ny))
                dfs(nx,ny,visit,n)
                visit.pop()


m = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
route = []
dfs(0,0,[(0,0)],len(m))
print(len(route))
for i in route:
    print(i)