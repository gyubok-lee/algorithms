# https://www.acmicpc.net/problem/17779

# 충분히 구상한뒤 코드로 이어갈것
def check(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

def border(x,y,d1,d2): # 경계선 마킹하기
    for i in range(d1+1):
        nx,ny = x +i, y-i
        if check(nx,ny) and my_board[nx][ny] == -1:
            my_board[nx][ny] = 5

    for i in range(d2+1):
        nx, ny = x+i,y+i
        if check(nx, ny) and my_board[nx][ny] == -1:
            my_board[nx][ny] = 5

    for i in range(d2+1):
        nx, ny = x+d1+i,y-d1+i
        if check(nx, ny) and my_board[nx][ny] == -1:
            my_board[nx][ny] = 5

    for i in range(d1+1):
        nx, ny = x+d2+i,y+d2-i
        if check(nx, ny) and my_board[nx][ny] == -1:
            my_board[nx][ny] = 5


def district(x,y,d1,d2): # 다른 선거구 마킹
    for i in range(N):
        dis5 = []
        for j in range(N):
            if my_board[i][j] == 5: # 한 행에서 경계선은 최대 두 개
                dis5.append((i, j))
                continue
            if 0<=i< x+d1 and 0<=j<=y:
                my_board[i][j] = 1
            elif 0<= i <= x+d2 and y<j<=N:
                my_board[i][j] = 2
            elif x+d1<=i<=N and 0<=j<y-d1+d2:
                my_board[i][j] = 3
            elif x+d2<=i<=N and y-d1+d2<=j<=N:
                my_board[i][j] = 4
            else:
                my_board[i][j] = 5

        if len(dis5) == 2: # 경계선 사이 칸들을 5로
            for k in range(dis5[0][1],dis5[1][1]):
                my_board[i][k] = 5

def counter() :
    res = [0,0,0,0,0]
    for i in range(N):
        for j in range(N):
            pos = my_board[i][j]-1
            res[pos] += board[i][j]
    return max(res) - min(res)

def select(d1,d2):
    global my_board

    for i in range(1,N):
        for j in range(2,N):
            my_board = [[-1] * N for _ in range(N)]
            border(i, j, d1, d2)
            district(i, j, d1, d2)
            ans.append(counter())


if __name__ == '__main__' :
    N = int(input())
    board = [list(map(int,input().split())) for i in range(N)]
    ans = []
    for d1 in range(1,N):
        for d2 in range(1,N):
            select(d1,d2)
    print(min(ans))
