# https://www.acmicpc.net/problem/14503

r, c = map(int,input().split())
robot = list(map(int,input().split()))
area = [list(map(int,input().split())) for i in range(r)]

left = [(0,-1), (-1,0), (0,1), (1,0)]
back = [(1,0), (0,-1), (-1,0), (0,1)]

x,y = robot[0], robot[1]
dir = robot[2]
res = 0
sw = True
while sw:
    if area[x][y] == 0:
        res += 1
        area[x][y] = 2
    cnt = 0
    while True:
        lx, ly = x + left[dir][0], y + left[dir][1]
        if area[lx][ly] == 0:
            dir = (dir+3)%4
            x, y = lx,ly
            break
        else:
            dir = (dir + 3) % 4
            cnt += 1

        if cnt == 4:
            bx, by = x + back[dir][0], y + back[dir][1]
            if area[bx][by] != 1:
                x,y = bx,by
            else :
                sw = False
            break
print(res)