# https://www.acmicpc.net/problem/15683

# 내 풀이
# cctv타입마다 모든 방향을 탐색하는 함수들을 더 효율적으로 해야함.
def backtracking(comb,depth,visit):
    global res
    angle_dict = { 1: [0,1,2,3], 2: [0,1], 3: [0,1,2,3],
                   4: [0,1,2,3], 5:[0]}

    if depth == len(cctv):
        cnt = len(run_cctv(comb,set()))
        if res < cnt :
            res = cnt
        return

    for i in range(depth,len(cctv)) :
        tv = cctv[i]
        if tv not in visit:
            for d in angle_dict[tv[0]]:
                comb.append((d,tv))
                visit.add(tv)
                backtracking(comb,depth+1,visit)
                comb.pop()
                visit.remove(tv)

def overview(order, r, c, see):

    if order == 0:
        for i in range(c, len(office[r])):
            if office[r][i] != 6:
                see.add((r, i))
            else:
                break
    elif order == 1:
        for i in range(r, len(office)):
            if office[i][c] != 6:
                see.add((i, c))
            else:
                break
    elif order == 2:
        for i in range(c, -1, -1):
            if office[r][i] != 6:
                see.add((r, i))
            else:
                break
    elif order == 3:
        for i in range(r, -1, -1):
            if office[i][c] != 6:
                see.add((i, c))
            else:
                break
    return see

def run_cctv(comb, see):
    for c in comb:
        angle = c[0]
        tv = c[1]
        if tv[0] == 1:
            if angle == 0 :
                see = overview(0, tv[1], tv[2], see)
            elif angle == 1:
                see = overview(1, tv[1], tv[2], see)
            elif angle == 2:
                see = overview(2, tv[1], tv[2], see)
            elif angle == 3:
                see = overview(3, tv[1], tv[2], see)
        elif tv[0] == 2:
            if angle == 0:
                see = overview(0, tv[1], tv[2], see)
                see = overview(2, tv[1], tv[2], see)
            elif angle == 1:
                see = overview(1, tv[1], tv[2], see)
                see = overview(3, tv[1], tv[2], see)

        elif tv[0] == 3:
            if angle == 0 :
                see = overview(0, tv[1], tv[2], see)
                see = overview(1, tv[1], tv[2], see)
            elif angle == 1:
                see = overview(1, tv[1], tv[2], see)
                see = overview(2, tv[1], tv[2], see)
            elif angle == 2:
                see = overview(2, tv[1], tv[2], see)
                see = overview(3, tv[1], tv[2], see)
            elif angle == 3:
                see = overview(3, tv[1], tv[2], see)
                see = overview(0, tv[1], tv[2], see)

        elif tv[0] == 4:
            if angle == 0 :
                see = overview(0, tv[1], tv[2], see)
                see = overview(1, tv[1], tv[2], see)
                see = overview(2, tv[1], tv[2], see)
            elif angle == 1 :
                see = overview(1, tv[1], tv[2], see)
                see = overview(2, tv[1], tv[2], see)
                see = overview(3, tv[1], tv[2], see)
            elif angle == 2 :
                see = overview(2, tv[1], tv[2], see)
                see = overview(3, tv[1], tv[2], see)
                see = overview(0, tv[1], tv[2], see)
            elif angle == 3 :
                see = overview(3, tv[1], tv[2], see)
                see = overview(0, tv[1], tv[2], see)
                see = overview(1, tv[1], tv[2], see)

        elif tv[0] == 5:
            see = overview(0, tv[1], tv[2], see)
            see = overview(1, tv[1], tv[2], see)
            see = overview(2, tv[1], tv[2], see)
            see = overview(3, tv[1], tv[2], see)
    return see

N, M = map(int,input().split())
cctv = []
office = []
walls = 0
for i in range(N):
    row = list(map(int,input().split()))
    office.append(row)
    for j in range(len(row)) :
        if row[j] != 0 and row[j] < 6 :
            cctv.append((row[j],i,j))
        elif row[j] == 6:
            walls += 1

res = 0
backtracking([],0,set())
print(N*M - res - walls)

# 모범풀이
'''
# 1. 각 cctv마다 각 방향에 대해 볼 수 있는 좌표들을 저장
# 2. 그 케이스들에 대해 dfs

import sys
input = sys.stdin.readline

def watch(x, y, direction): #해당방향으로 벽이 나올때까지 찾음
    ret = set()
    for d in direction:  # 0 ~ 3 : 북, 동, 남, 서
        new_x, new_y = x + dx[d], y + dy[d]
        while 0 <= new_x < N and 0 <= new_y < M:
            if office[new_x][new_y] == 6: break
            if office[new_x][new_y] == 0: ret.add((new_x, new_y))
            new_x, new_y = new_x + dx[d], new_y + dy[d]

    return ret


def dfs(n, watched_set):
    global max_watched_cnt
    if n == len(cctvs_cases):
        if max_watched_cnt < len(watched_set):
            max_watched_cnt = len(watched_set)
        return
    for cctv_cases in cctvs_cases[n]: # 각 cctv에 대해
        dfs(n + 1, watched_set | cctv_cases)


cctvs_cases = []  # 각 cctv의 가능한 케이스

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)  # 동서남북, 좌표 이동 백터

N, M = map(int, input().split())  # N: 세로, M: 가로
office = [[*map(int, input().split())] for _ in range(N)]  # cctv, 벽 정보

will_watched_cnt = 0
for idx in range(N * M): # 입력자체를 모든경우의 수를 세서 받음
    i, j = divmod(idx, M)
    if office[i][j] == 0:
        will_watched_cnt += 1
    elif office[i][j] == 1:
        cctvs_cases.append([watch(i, j, [v]) for v in range(4)])
    elif office[i][j] == 2:
        cctvs_cases.append([watch(i, j, [v % 4, (v + 2) % 4]) for v in range(2)])
    elif office[i][j] == 3:
        cctvs_cases.append([watch(i, j, [v % 4, (v + 1) % 4]) for v in range(4)])
    elif office[i][j] == 4:
        cctvs_cases.append([watch(i, j, [(_ + v) % 4 for _ in range(3)]) for v in range(4)])
    elif office[i][j] == 5:
        cctvs_cases.append([watch(i, j, [0, 1, 2, 3])])

max_watched_cnt = 0
dfs(0, set())  # 감시 가능한 최대 영역 개수

print(will_watched_cnt - max_watched_cnt)  # 최소 사각지대 개수
'''