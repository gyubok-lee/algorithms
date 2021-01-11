# https://www.acmicpc.net/problem/1697

from collections import deque

N, K = map(int,input().split())
arr = [100000] * 100001
arr[N] = 0
que = deque([N])
while True:
    now = que.popleft()
    if now == K :
        print(arr[K])
        break
    walk_front = now + 1
    walk_back = now - 1
    blink = now * 2

    if walk_front <= 100000 :
        if arr[walk_front] == 100000:
            arr[walk_front] = arr[now]+1
            que.append(walk_front)
    if walk_back >= 0 :
        if arr[walk_back] == 100000:
            arr[walk_back] = arr[now]+1
            que.append(walk_back)
    if now != 0 and blink <= 100000:
        if arr[blink] == 100000:
            arr[blink] = arr[now]+1
            que.append(blink)




