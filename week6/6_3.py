# https://programmers.co.kr/learn/courses/30/lessons/67259

# 동적계획법 + bfs
'''
1. 이미 방문한 칸이라도 최소비용을 확인해봐야하기때문에 visit은 없어도 됨.
2. 해당단계까지의 최적해를 구하는 문제는 동적계획법이라고 생각할 것.
3. dfs를 활용한 모든경로 탐색에 취약했음.
'''

from collections import deque

def bfs(n, board):
    init_num = 100e9
    arr = [[init_num] * n for i in range(n)]
    arr[0][0] = 0
    q= deque([(0,0,0,0)])
    cand = []
    deltas = [(1, 0, 1), (0, 1, 2), (-1, 0, 3), (0, -1, 4)]

    while q :
        x,y,charge,change = q.popleft()
        if x == n-1 and y == n-1 :
            cand.append(charge)

        for d in deltas :
            nx, ny = x+d[0], y+d[1]
            if change != 0 and change != d[2]:
                add_charge = 600
            else:
                add_charge = 100
            if 0<=nx<n and 0<=ny<n and board[ny][nx] == 0:
                if arr[ny][nx] < charge + add_charge :
                    continue
                q.append((nx,ny,charge+add_charge,d[2]))
                arr[ny][nx] = charge + add_charge
    return min(cand)


def solution(board):
    return bfs(len(board),board)

b = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

print(solution(b))