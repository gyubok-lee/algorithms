# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque
def bfs(start,v,arr,cnt):
    que = deque([start])
    while que:
        print(que, v)
        now = que.popleft()
        for i in range(len(arr[now])):
            if i == now :
                continue
            if arr[now][i] == 1 and v[i] == 0 :
                v[i] = cnt
                que.append(i)
    return v

def solution(n, computers):
    visited = [0] * n
    cnt = 1
    for i in range(n):
        print("now: ", i)
        if visited[i] == 0:
            visited[i] = cnt
            visited = bfs(i,visited,computers,cnt)
            cnt+=1
    return max(visited)

nn = 3
coms = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(nn,coms))