# https://programmers.co.kr/learn/courses/30/lessons/60063

# visit 배열을 안써도 set을 활용해 중복을 막을 수 있다.
# 해당단계에서 할 수 있는 모든 작업을 하면서, 깊이가 곧 이동수
from collections import deque

def check(leg1, leg2, arr):
    X, Y = 1,0
    cand = []

    # 이동
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in directions:
        next1 = (leg1[Y] + dy, leg1[X] + dx)
        next2 = (leg2[Y] + dy, leg2[X] + dx)
        if arr[next1[Y]][next1[X]] == 0 and arr[next2[Y]][next2[X]] == 0:
            cand.append((next1, next2))
    # 회전
    if leg1[Y] == leg2[Y]: # 가로
        for d in [-1, 1]:
            if arr[leg1[Y] + d][leg1[X]] == 0 and arr[leg2[Y] + d][leg2[X]] == 0:
                cand.append((leg1, (leg1[Y] + d, leg1[X])))
                cand.append((leg2, (leg2[Y] + d, leg2[X])))
    else:
        for d in [-1, 1]:
            if arr[leg1[Y]][leg1[X] + d] == 0 and arr[leg2[Y]][leg2[X] + d] == 0:
                cand.append(((leg1[Y], leg1[X] + d), leg1))
                cand.append(((leg2[Y], leg2[X] + d), leg2))

    return cand

def solution(board):
    # board 외벽 둘러싸기
    N = len(board)
    arr = [[1] * (N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            arr[i+1][j+1] = board[i][j]

    # 루트
    que = deque([((1, 1), (1, 2), 0)])
    route = set([((1, 1), (1, 2))])

    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return count
        for next in check(cur1, cur2, arr):
            if next not in route:
                que.append((*next, count+1)) # unpacking, 깊이 증가
                route.add(next)

b = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(b))