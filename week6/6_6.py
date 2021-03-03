# https://www.acmicpc.net/problem/16234

# PS 설계부터 제대로 할 것
'''
1. 모든 국가들에 대해
2. 연합될수 있는 국가들을 모두 찾고
3. 인구를 분배
4. 1~3 과정을 새로운 연합이 없을 때까지 반복
'''
from collections import deque

def bfs(x, y):
    deltas = [(1,0),(-1,0),(0,1),(0,-1)]
    united = []
    q.append((x, y))
    visit.add((x,y))
    people, num = 0, 0

    while q: # 연합되는 국가들 찾기
        x, y = q.popleft()
        united.append((x, y))
        people += nations[x][y]
        num += 1
        for delta in deltas:
            nx,ny = x + delta[0], y + delta[1]
            if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in visit:
                if L <= abs(nations[x][y] - nations[nx][ny]) <= R:
                    visit.add((nx,ny))
                    q.append((nx, ny))

    while united: # 인구 분배
        x, y = united.pop()
        nations[x][y] = people // num

    if num == 1: # 새로운 연합이 없을 경우
        return 0
    return 1

N,L,R = map(int,input().split())
nations = [list(map(int,input().split())) for i in range(N)]

ans = 0
while True:
    q = deque()
    visit = set()
    cnt = 0

    # 모든 국가들에 대해
    for i in range(N):
        for j in range(N):
            if (i,j) not in visit:
                cnt += bfs(i, j) #새로 연합이 되는 국가가 있는지
    if cnt == 0: # 전체 국가들중 새로운 연합이 없다면
        break
    ans += 1
print(ans)