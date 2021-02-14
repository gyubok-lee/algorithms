# https://www.acmicpc.net/problem/2164

from collections import deque
N = int(input())
que = deque([i+1 for i in range(N)])

while len(que) > 1 :
    que.popleft()
    to_below = que.popleft()
    que.append(to_below)
print(que[0])
