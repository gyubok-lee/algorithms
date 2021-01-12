# https://www.acmicpc.net/problem/7562

from collections import deque

def check(x,y,n,v):
    if (x,y) in v :
        return False
    if 0<=x<n and 0<=y<n :
        return True
    else :
        return False

def bfs(n,start,target):
    que = deque([(*start,0)])
    visited = set([start])

    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]

    while que:
        x,y,cnt = que.popleft()
        if x == target[0] and y == target[1] :
            return cnt
        for i in range(8) :
            nx, ny = x+dx[i], y+dy[i]
            if check(nx,ny,n,visited) :
                que.append((nx,ny,cnt+1))
                visited.add((nx,ny))

    return

cases = int(input())
for i in range(cases):
    n = int(input())
    start = tuple(map(int,input().split()))
    target = tuple(map(int,input().split()))
    print(bfs(n,start,target))