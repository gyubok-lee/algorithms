# https://www.acmicpc.net/problem/19238

# 첫번째 테스트 케이스가 틀림.. 원인을 모르겠음
# 승객을 고르는 함수에서 오류가 있을듯함.
from collections import deque

def choose_user(pos):
    q = deque([(*pos,0)])
    visit = set([pos])
    res = []

    while q:
        x,y,cnt = q.popleft()
        if cnt > gas and len(res) == 0:
            return res

        if (x,y) in users: # 손님을 찾았다면
            if len(res) >= 1: # 후보가 있다면
                if cnt > res[-1][2]:
                    break
                elif x > res[-1][0] :
                    break
                elif y > res[-1][1] :
                    break
                res = [(x,y,cnt)]
            else:
                res = [(x,y,cnt)]

        for delta in deltas :
            nx,ny = x+delta[0], y+delta[1]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] != 1:
                if (nx,ny) not in visit :
                    q.append(((nx,ny,cnt+1)))
                    visit.add((nx,ny))
    return res

def go(pos,dest):
    q = deque([(*pos, 0)])
    visit = set([pos])

    while q:
        x, y, cnt = q.popleft()
        if cnt > gas :
            return -1
        if x == dest[0] and y == dest[1] :
            return cnt

        for delta in deltas :
            nx,ny = x+delta[0], y+delta[1]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] != 1:
                if (nx,ny) not in visit :
                    q.append(((nx,ny,cnt+1)))
                    visit.add((nx, ny))
    return -1

if __name__ == '__main__' :
    N, M , gas = map(int,input().split())
    board = [list(map(int,input().split())) for i in range(N)]
    start = tuple(i-1 for i in map(int,input().split()))

    users = set()
    users_info = dict()
    for i in range(M):
        x1,y1,x2,y2 = map(int,input().split())
        users_info[(x1-1,y1-1)] = (x2-1,y2-1)
        users.add((x1-1,y1-1))


    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ride = ()
    sw = True
    for i in range(M):
        now_user = choose_user(start)
        #print('\n','출발지: ', start)
        if len(now_user) == 0:
            sw = False
            break
        else :
            gas -= now_user[0][2]
            ride = (now_user[0][0],now_user[0][1])
            users.remove(ride)
        #print('손님: ', ride)
        #print('태우러 가면서 남은 가스:',gas)
        cond = go(ride,users_info[ride])
        if cond == -1:
            sw = False
            break
        else:
            gas += cond
            start = users_info[ride]
            #print('목적지:', start)
        #('이후 남은 가스:',gas)

    print(gas if sw else -1)
