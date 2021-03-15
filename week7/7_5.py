# https://www.acmicpc.net/problem/17822
from collections import deque

def roll(xs, d, k) : # 원판 돌리기
    for i in range(len(circles)) :
        if (i+1) % xs == 0:
            new_row = deque(circles[i])

            if d == 0:
                for _ in range(k):
                    new_row.appendleft(new_row.pop())
            elif d == 1:
                for _ in range(k):
                    new_row.append(new_row.popleft())
            circles[i] = list(new_row)
    return

def bfs(): # 인접한 같은 수 찾기
    visit = set() # 전체 숫자 중 방문한 곳 마킹
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    changed = False # 한번이라도 삭제가 됐는지

    for i in range(N):
        for j in range(M):
            if (i,j) in visit or circles[i][j] == 0:
                continue

            q = deque([(i,j)])
            target = circles[i][j]
            same = []

            while q:
                now = q.popleft()
                for delta in deltas :
                    nx, ny = now[0] + delta[0], now[1]+delta[1]

                    # 순환큐 고려
                    if nx == -1 or nx == N:
                        continue
                    if ny == -1:
                        ny = M-1
                    elif ny == M:
                        ny = 0

                    # 인접한 좌표에 대해 bfs
                    if circles[nx][ny] == target and (nx,ny) not in visit:
                        visit.add((nx,ny))
                        same.append((nx,ny))
                        q.append((nx,ny))

            if len(same):
                visit.add((i,j))
                same.append((i,j))
                changed = True
                for _ in same:
                    circles[_[0]][_[1]] = 0
    return changed

def modify(): # 숫자 바꾸기
    non_zeros = []
    s = 0
    cnt = 0

    for i in range(N):
        for j in range(M):
            if circles[i][j] != 0:
                s += circles[i][j]
                cnt += 1
                non_zeros.append((i,j))
    if cnt == 0:
        return

    avg = s / cnt
    for x,y in non_zeros:
        if circles[x][y] > avg:
            circles[x][y] -= 1
        elif circles[x][y] < avg:
            circles[x][y] += 1
    return

if __name__ == '__main__' :
    N,M,T = map(int,input().split())
    circles = [list(map(int,input().split())) for i in range(N)]
    commands = [list(map(int,input().split())) for i in range(T)]
    ans = 0

    for command in commands:
        roll(command[0],command[1], command[2])
        if not bfs(): # 삭제되는 숫자가 없다면
            modify()

    for i in range(N):
        ans += sum(circles[i])
    print(int(ans))