# https://www.acmicpc.net/problem/14502
"""
1. 최대 깊이에 닿았을때
2. 일반 연산 후 재귀
3. 표식이 있었다면 제거
4. 표식은 행해준 같은 인덴트안에서 지워주면 됨.

"""
from collections import deque
def finder(depth):
    global arr
    global zeros
    global visited

    if depth == 3:
        infection(arr)
        return

    for _ in range(len(zeros)) :
        if visited[_] == 0:
            arr[zeros[_][0]][zeros[_][1]] = 1
            visited[_] = 1
            finder(depth+1)
            arr[zeros[_][0]][zeros[_][1]] = 0
            visited[_] = 0
    return

def infection (a):
    global max_size

    dir = [ (-1,0), (1,0), (0,-1), (0,1) ]

    # 깊은 복사
    sim= [a[i][:] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if sim[i][j] == 2:
                que.append([i, j])

    # 시뮬레이션
    while que:
        x,y = que.popleft()
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0<= nx <n and 0<= ny < m:
                if sim[nx][ny] == 0 :
                    sim[nx][ny] = 2
                    que.append([nx,ny])
    cnt = 0
    for i in sim:
        cnt += i.count(0)
    max_size = max(max_size, cnt)

    return

n, m = map(int, input().split())
arr = []
virus = []
zeros = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            virus.append([i,j])
        elif row[j] == 0:
            zeros.append([i,j])
    arr.append(row)

visited = [0]* len(zeros)
max_size = 0
que = deque()
finder(0)
print(max_size)