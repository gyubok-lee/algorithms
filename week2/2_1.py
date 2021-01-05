# https://www.acmicpc.net/problem/14499

# 시물레이션 : 파악만하면 됨.
N, M, x, y, order_num = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
orders = list(map(int,input().split()))

dice = [0,0,0,0,0,0]
dx = [0, 0, -1, 1] # 동서
dy = [1, -1, 0, 0] # 남북

for i in range(order_num):
    dir = orders[i] - 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not 0 <= nx < N or not 0 <= ny < M:
        continue

    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[5]
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])
