# https://www.acmicpc.net/problem/17144

# 과도한 반복문은 자제할 것.

def get_purifier():
    for i in range(R):
        if board[i][0] == -1:
            return [i, 0], [i + 1, 0]

def diffusion() :
    dust = [[0] * C for _ in range(R)]
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(R):
        for j in range(C):
            if board[i][j] >= 5:
                val = 0
                for delta in deltas:
                    nx, ny = i+delta[0], j+delta[1]
                    if 0<=nx<R and 0<= ny<C:
                        if board[nx][ny] != -1:
                            dust[nx][ny] += board[i][j] // 5
                            val += board[i][j] // 5
                dust[i][j] -= val

    for i in range(R):
        for j in range(C):
            board[i][j] += dust[i][j]

    return

def operation(up,down):
    # up
    for i in range(up[0] - 2, -1, -1):
        board[i + 1][0] = board[i][0]
    for i in range(1, C):
        board[0][i - 1] = board[0][i]
    for i in range(1, up[0] + 1):
        board[i - 1][-1] = board[i][-1]
    for i in range(C - 2, 0, -1):
        board[up[0]][i + 1] = board[up[0]][i]
    board[up[0]][1] = 0

    # down
    for i in range(down[0] + 2, R):
        board[i - 1][0] = board[i][0]
    for i in range(1, C):
        board[-1][i - 1] = board[-1][i]
    for i in range(R - 2, down[0] - 1, -1):
        board[i + 1][-1] = board[i][-1]
    for i in range(C - 2, 0, -1):
        board[down[0]][i + 1] = board[down[0]][i]
    board[down[0]][1] = 0

    return

def run() :
    up,down = get_purifier()

    for i in range(T):
        diffusion()
        operation(up,down)

    res = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] != -1:
                res += board[i][j]
    return res

R,C,T = map(int,input().split())
board = [list(map(int,input().split())) for i in range(R)]
print(run())

