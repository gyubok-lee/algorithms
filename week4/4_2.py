# https://www.acmicpc.net/problem/2644

from collections import deque

def finder(person):
    cand = []
    for i in range(len(relationship[person])):
        if relationship[person][i] == 1:
            cand.append(i)
    return cand

def BFS() :
    while que:
        now, count = que.popleft()
        if now == end:
            return count
        for next in finder(now):
            if next not in route:
                que.append((next, count + 1))
                route.add(next)
    return -1

n = int(input())
start, end = map(int,input().split())
m = int(input())

relationship = [[0] * (n+1) for i in range(n+1)]
for i in range(m) :
    parent, child = map(int,input().split())
    relationship[parent][child] = 1
    relationship[child][parent] = 1

que = deque([(start,0)])
route = set([start])
print(BFS())




