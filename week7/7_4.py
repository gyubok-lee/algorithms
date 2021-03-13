# https://www.acmicpc.net/problem/16236

from collections import deque

def check(x,y,size, visit):
    if 0<=x<N and 0<=y<N and (x,y) not in visit:
        if space[x][y] <= size:
            return True
    return False

def comp(lst,x,y,cnt): # 물고기 우선순위 정하기
    if len(lst) == 0:
        lst = [[x, y, cnt]]
    else:
        if lst[0][2] < cnt:
            return lst, 0
        else:
            if lst[0][0] > x:
                lst = [[x, y, cnt]]
            elif lst[0][0] == x and lst[0][1] > y:
                lst = [[x, y, cnt]]
    return lst, 1

def move(pos,size):
    q= deque([[pos[0],pos[1],0]])
    visit = set([(pos[0],pos[1])])
    res = []
    sw = False

    # 더 먹을 수 있는 물고기가 있는지
    for i in fishes :
        if i[2] < size :
            sw = True
            break
    if not sw :
        return res

    while q:
        x,y,cnt = q.popleft()

        if [x, y, space[x][y]] in fishes : # 물고기를 찾았자면
            if space[x][y] < size:
                res, b = comp(res,x,y,cnt)
                if not b : break

        for delta in deltas:
            nx, ny = x+delta[0], y+ delta[1]
            if check(nx,ny,size,visit) :
                q.append([nx,ny,cnt+1])
                visit.add((nx,ny))
    return res


if __name__ == '__main__' :
    N = int(input())
    shark = []
    fishes = []
    space = []
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(N):
        row = list(map(int,input().split()))
        for j in range(N):
            if row[j] == 9:
                shark = [i,j]
                row[j] = 0
            elif row[j] != 0:
                fishes.append([i,j,row[j]])
        space.append(row)

    cnt = 0
    shark_size = 2
    exp = 0
    while True:
        eat = move(shark,shark_size)
        if len(eat) == 0:
            break
        fishes.remove([eat[0][0], eat[0][1], space[eat[0][0]][eat[0][1]]])
        shark = [eat[0][0], eat[0][1]]

        cnt += eat[0][2]
        exp += 1
        if exp == shark_size:
            shark_size += 1
            exp =0
    print(cnt)


