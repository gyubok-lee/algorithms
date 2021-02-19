# https://www.acmicpc.net/problem/1753

# 최단경로 : Dijkstra 알고리즘
# pypy3로 통과
def Dijkstra(start):
    global V
    visit = set([start])
    dist = [1000000] * (V+1)

    # 초기화
    for i in graph[start]:
        dist[i] = graph[start][i]

    while len(visit) < V : # 모든 정점에 대해서
        u = find_next(dist, visit) # 가장 가중치가 작은 정점
        if u == -1: # 더이상 연결된 정점이 없다면 break
            break
        visit.add(u)

        for z in graph[u]:
            if z not in visit :
                if dist[u] + graph[u][z] < dist[z] : # 현재의 거리보다 경유거리가 더 가깝다면
                    dist[z] = dist[u] + graph[u][z]
    return dist

def find_next(dist, visit) :
    m = 1000000
    next = -1
    for i in range(1,len(dist)):
        if dist[i] < m and i not in visit :
            m = dist[i]
            next = i
    return next

# 입력
V, E = map(int,input().split())
K = int(input())
graph = [{} for i in range(V+1)]

for i in range(E):
    u,v,w = map(int,input().split())
    if v in graph[u] :
        graph[u][v] = min(graph[u][v],w)
    else :
        graph[u][v] = w

# 출력
res = Dijkstra(K)
for i in range(1,len(res)):
    if i == K :
        print(0)
    elif res[i] >= 1000000 :
        print('INF')
    else :
        print(res[i])

