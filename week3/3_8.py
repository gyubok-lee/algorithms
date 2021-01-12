# https://www.acmicpc.net/problem/2630

def check(x,y,n):
    if n == 1:
        return True

    for i in range(n):
        for j in range(n):
            if board[x+i][y+j] != board[x][y]:
                return False
    return True

def divide(node):
    global blue
    global white

    x,y,size = node
    if check(x,y,size):
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
    else :
        ns = int(size/2)
        quadTree[node] = [(x,y,ns),(x+ns,y,ns),(x,y+ns,ns),(x+ns,y+ns,ns)]
        for i in quadTree[node]:
            divide(i)
    return

N = int(input())
board = [list(map(int,input().split())) for i in range(N)]
quadTree = dict()
blue = 0
white = 0

divide((0,0,N))
print(white)
print(blue)