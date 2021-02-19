# https://programmers.co.kr/learn/courses/30/lessons/72413

INF = 99999999

def Dijkstra(n, start,g):
    visit = set([start])
    dist = [INF] * (n+1)

    # 초기화
    for i in range(1,n+1):
        dist[i] = g[start][i]

    while len(visit) < n : # 모든 정점에 대해서
        u = find_next(dist, visit) # 가장 가중치가 작은 정점
        if u == -1: # 더이상 연결된 정점이 없다면 break
            break
        visit.add(u)

        for z in range(1,n+1):
            if z not in visit :
                if dist[u] + g[u][z] < dist[z] : # 현재의 거리보다 경유거리가 더 가깝다면
                    dist[z] = dist[u] + g[u][z]

    dist[start] = 0
    return dist

def find_next(dist, visit) :
    m = INF
    next = -1
    for i in range(1,len(dist)):
        if dist[i] < m and i not in visit :
            m = dist[i]
            next = i
    return next

def solution(n, s, a, b, fares):
    # 입력
    graph = [[INF] * (n + 1) for i in range(n + 1)]
    for i in fares :
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]

    # 경유지
    both = Dijkstra(n, s, graph)

    # 경유지에서 각자의 집까지
    min_dist = INF
    for mid in range(1,n+1) :
        to_go = Dijkstra(n, mid, graph)
        now = to_go[a] + to_go[b] + both[mid]
        if now < min_dist :
            min_dist = now

    return min_dist

n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n, s, a, b, fares))