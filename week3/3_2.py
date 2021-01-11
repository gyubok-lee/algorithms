# N-queen

# 백트레킹 관련문제
def nQueen(row, n):
    global cnt
    if row == n:
        cnt += 1
        return

    for i in range(n):
        chess[row] = i
        if checker(row):
            nQueen(row + 1, n)

def checker(row):
    for i in range(row):
        if (chess[row] == chess[i]) or (abs(chess[row] - chess[i]) == row - i):
            return False
    return True

def solution(n):
    global chess
    global cnt

    chess = [-1] * n
    cnt = 0
    nQueen(0, n)
    return cnt

print(solution((4)))