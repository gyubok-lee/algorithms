# https://www.acmicpc.net/problem/17142

# 2차원 배열을 만드는 과정은 생각보다 시간이 별로 안걸린다.
# visit을 배열로 사용해도 무방

from itertools import combinations
from collections import deque

def check(x,y):
    if 0<=x<N and 0<=y<N :
        if lab[x][y] != 1 and (x,y) not in visit :
            return True
    return False

def spread(comb):
    global visit
    que = deque()
    max_cnt = 0
    not_visit = N*N
    visit = set()

    for _ in comb:
        que.append(_)
        visit.add((_[0],_[1]))

    while que:
        x,y,t = que.popleft()
        not_visit -= 1
        for delta in deltas:
            nx, ny = x + delta[0], y + delta[1]
            if check(nx,ny):
                visit.add((nx,ny))
                if lab[nx][ny] == 0:
                    max_cnt = max(max_cnt,t+1)
                que.append((nx,ny,t+1))

    if len(visit)+walls == N*N: # 모든 칸에 확산된 경우에만
        ans.append(max_cnt)

if __name__ == "__main__":
    N, M = map(int,input().split())
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    lab = []
    virus = []
    ans = []
    walls = 0

    for i in range(N):
        row = list(map(int,input().split()))
        for j in range(N):
            if row[j] == 2:
                virus.append((i,j,0))
            elif row[j] == 1:
                walls += 1
        lab.append(row)

    for comb in combinations(virus,M):
        spread(comb)
    print(min(ans) if ans else -1)