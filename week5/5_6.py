# https://programmers.co.kr/learn/courses/30/lessons/72415

# 실패... 아래는 모범코드
from itertools import permutations
from collections import deque

''' 해설
1. 찾을 카드 순서들의 순열을 만든다. (init)
2. 각 순열의 조합마다, 아래와 같은 절차를 수행한다 (backtracking)
    2-1. 시작지점에서 다음 카드 순서쌍들을 제거하는 이동횟수를 구한다.
    2-2. 카드1->카드2 / 카드2->카드1 두 가지 경우의 수가 있으니 두 경우 모두에 대해 백트레킹.
3. 이동횟수를 구하는 로직은 다음과 같다(bfs)
    3-1. 해당지점에서 단순히 상하좌우로 한칸씩 이동할 수 있는 칸들을 큐에 넣는다
    3-2. 해당지점에서 ctrl+방향키로 이동할수 있는 칸들을 큐에 넣는다.
'''

'''
브루트포스 + 백트레킹 + bfs를 모두 활용해야하는 시뮬레이션 문제.

전반적인 풀이방법은 알았지만, 실제로 구현하기 어려웠음. 특히 이동횟수를 구하는 bfs를 발상못함.
심화된 백트레킹 풀이도 발상못했을듯.

복잡한 문제일수록 문제 풀이 구도를 먼저 잡고 접근하려는 노력이 필요.
'''

size = 4
myboard = [[] for i in range(4)]
card_pos = {}
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
INF = int(1e4)
answer = INF
orders = []

def init(board):
    global myboard, card_pos, orders
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0:
                card = board[i][j]
                if card not in card_pos.keys():
                    card_pos[card] = [[i, j]]
                else:
                    card_pos[card].append([i, j])

            myboard[i].append(board[i][j])
    orders = list(permutations(card_pos.keys()))


# 이동한 결과가 보드 범위내 있는지 판단하는 함수
def isin(y, x):
    if -1 < y < size:
        if -1 < x < size:
            return True
    return False

# ctrl + 방향키
def move(y, x, mv):
    global myboard
    ny, nx = y, x

    while True:
        _ny = ny + mv[0]
        _nx = nx + mv[1]

        if not isin(_ny, _nx): # 이동이 유요하지 않다면
            return ny, nx

        if myboard[_ny][_nx] != 0: # 이동한 곳이 카드라면
            return _ny, _nx

        ny = _ny
        nx = _nx
    return ny, nx


# 카드 1장을 찾을 때 나오는 거리를 반환하는 함수(목표 위치도 반환함)
# 시작 위치: myboard[sy, sx], 찾아야 할 위치: myboard[ey, ex]
def bfs(sy, sx, ey, ex):
    global myboard

    if [sy, sx] == [ey, ex]:
        return sy, sx, 1

    q = deque([[sy, sx]])
    table = [[0 for j in range(size)] for i in range(size)]
    visit = [[False for j in range(size)] for i in range(size)]
    visit[sy][sx] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            # 일반 이동(상하좌우)
            if isin(ny, nx):
                if not visit[ny][nx]:
                    visit[ny][nx] = True
                    table[ny][nx] = table[y][x] + 1
                    if [ny, nx] == [ey, ex]:
                        return ny, nx, table[ny][nx] + 1

                    q.append([ny, nx])

            # ctrl + 이동
            ny, nx = move(y, x, d[i])
            if not visit[ny][nx]:
                visit[ny][nx] = True
                table[ny][nx] = table[y][x] + 1
                if [ny, nx] == [ey, ex]:
                    return ny, nx, table[ny][nx] + 1

                q.append([ny, nx])

    return sy, sx, INF


# 찾은 2장의 카드를 myboard에서 지워주는 함수
def remove(card):
    global myboard, card_pos
    for y, x in card_pos[card]:
        myboard[y][x] = 0

# 지워진 2장의 카드를 myboard에서 복원해주는 함수
def restore(card):
    global myboard, card_pos
    for y, x in card_pos[card]:
        myboard[y][x] = card


# backtracking
# 현재위치, 깊이, m번째 조합, 카운트
# 현재->카드1->카드2 / 현재->카드2->카드1 두가지 모두 살펴봄
def backtrack(sy, sx, k, m, count):
    global orders, myboard, answer, card_pos

    if k == len(card_pos.keys()):
        if answer > count:
            answer = count
        return

    card = orders[m][k]
    left_y, left_x = card_pos[card][0][0], card_pos[card][0][1]
    right_y, right_x = card_pos[card][1][0], card_pos[card][1][1]

    # ----------------------------------------------
    ry1, rx1, res1 = bfs(sy, sx, left_y, left_x)
    ry2, rx2, res2 = bfs(ry1, rx1, right_y, right_x)

    remove(card)
    backtrack(ry2, rx2, k + 1, m, count + res1 + res2)
    restore(card)

    # ----------------------------------------------
    ry1, rx1, res1 = bfs(sy, sx, right_y, right_x)
    ry2, rx2, res2 = bfs(ry1, rx1, left_y, left_x)

    remove(card)
    backtrack(ry2, rx2, k + 1, m, count + res1 + res2)
    restore(card)


def solution(board, r, c):
    global answer
    init(board)

    for i in range(len(orders)):
        backtrack(r, c, 0, i, 0)

    return answer

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
print(solution(board,r,c))