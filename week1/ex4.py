#https://www.acmicpc.net/problem/3190

def checker (togo,limit):
    global m
    global snake
    for i in togo:
        if i >= limit or i < 0:
            return False
    if m[togo[0]][togo[1]] == 2:
        return False
    else :
        if m[togo[0]][togo[1]] == 1:
            snake.insert(0,togo)
        if m[togo[0]][togo[1]] == 0:
            snake.insert(0, togo)
            snake.pop()
        return True

size = int(input())
m = [[0] * size for i in range(size)]

# 사과 위치
apple_num = int(input())
for i in range(apple_num):
    x,y = map(int,input().split())
    m[x-1][y-1] = 1

# 뱀의 이동
command_num = int(input())
command = []
for i in range(command_num):
    cm = input().split()
    cm[0] = int(cm[0])
    command.append(cm)

# 플레이
snake = [[0,0]]
direction = 1
cnt = 0
while True:
    cnt += 1
    body = []
    for _ in snake :
        m[_[0]][_[1]] = 2
        body.append(_)

    headX, headY = snake[0][0], snake[0][1]
    if direction == 3:
        next = [headX,headY-1]
        if(checker(next,size) == False):
            break
    elif direction == 1 :
        next = [headX,headY+1]
        if (checker(next, size) == False):
            break
    elif direction == 0 :
        next = [headX-1,headY]
        if (checker(next, size) == False):
            break
    elif direction == 2 :
        next = [headX+1,headY]
        if (checker(next, size) == False):
            break

    if (len(command) >0) and (cnt == command[0][0]) :
        if command[0][1] == 'D':
            direction = (direction+1) % 4
        else :
            direction = (direction - 1) % 4
        command.pop(0)
    for _ in body :
        m[_[0]][_[1]] = 0

print(cnt)