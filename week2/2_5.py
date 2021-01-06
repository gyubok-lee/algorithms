def tornado(n,m) :
    global res
    now = field[n][m]
    a = now
    field[n][m] = 0


    for i in range(len(effect)-1) :
        nx, ny = n + effect[i][0], m+ effect[i][1]
        if 0<=nx<N and 0<=ny<N :
            field[nx][ny] += int(now * sand[i])
            a -= int(now * sand[i])
        else :
            a -= int(now * sand[i])
            res += int(now * sand[i])


    nx, ny = n + effect[-1][0], m + effect[-1][1]
    if 0 <= nx < N and 0 <= ny < N:
        field[nx][ny] += a
    else:
        res += a
    return

def rotate():
    for i in effect:
        i[0] ,i[1] = i[1]* -1, i[0]
    to[0], to[1] = to[1] * -1, to[0]
    return

effect = [[-2,0],[-1,-1],[-1,0],[-1,1],[0,-2],
          [1,-1],[1,0],[1,1],[2,0],[0,-1]]
sand = [0.02,0.1,0.07,0.01,0.05,0.1,0.07,0.01,0.02,0.55]
to = [0,-1]
direction = 0

N = int(input())
field = [list(map(int,input().split())) for i in range(N)]
x,y = int(N /2),int(N /2)

res = 0
for _ in range(1,N) :
    if _ < N-1 :
        for i in range(2):
            for j in range(_):
                x , y = x+ to[0],y+ to[1]
                tornado(x,y)
            rotate()
    else:
        for i in range(3) :
            for j in range(_):
                x, y = x + to[0], y + to[1]
                tornado(x, y)
            rotate()
print(res)


