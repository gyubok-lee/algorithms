# https://www.acmicpc.net/problem/1967
"""
# 백트래킹을 이용한 풀이: 메모리초과.
def finder(start,path,visited,dist):
    global nodes
    global N
    global idx
    global res
    global max_dist

    now = path[-1]
    if (now != start) and (now in idx) :
        temp = path.copy() #
        one = sum(dist)
        if one > max_dist :
            max_dist = one
        res.append(temp)
        return

    for i in range(N):
        if nodes[now][i] != 0 and visited[i] ==0:
            path.append(i)
            dist.append(nodes[now][i])
            visited[i] = 1

            finder(start,path,visited,dist)
            path.pop()
            dist.pop()
            visited[i] = 0

        if nodes[i][now] != 0 and visited[i] ==0:
            path.append(i)
            dist.append(nodes[i][now])
            visited[i] = 1
            finder(start,path,visited,dist)
            path.pop()
            dist.pop()
            visited[i] = 0
    return

N = int(input())
is_leaf = [1] * N
nodes = [[0] * N for i in range(N)]
for i in range(N-1):
    parent, child, weight = map(int,input().split())
    nodes[parent-1][child-1] = weight
    is_leaf[parent-1] = 0


idx = [i for i in range(N) if is_leaf[i] == 1]
v = [0] * N

max_dist = 0
for i in range(len(idx)):
    res = []
    finder(idx[i],[idx[i]],v,[])
    #print(res)
print(max_dist)
"""

# 풀이: 임의의 노드 A에서 가장 먼 노드 B와 B에서 가장 먼 노드 C가 지름

def farthest(i): # 가장 먼 노드 찾기
    stack = tree[i][:]
    visit = [False] * (N+1)
    visit[i] = True
    node, dist = 0, 0

    # B찾기
    for sn, sd in stack:
        visit[sn] = True
        if sd > dist:
            node = sn
            dist = sd

    while stack:
        sn, sd = stack.pop()
        link = tree[sn]
        for ln, ld in link:
            if not visit[ln]:
                visit[ln] = True
                now = sd + ld
                stack.append((ln, now))
                if now > dist:
                    node = ln
                    dist = now
    return node, dist

N = int(input())
tree = {}
key = []
for i in range(N-1):
    n1, n2, weight = map(int,input().split())
    tree.setdefault(n1,[])
    tree.setdefault(n2, [])
    tree[n1].append((n2,weight))
    tree[n2].append((n1, weight))
if len(tree) == 0:
    print(0)
else:
    edge, dist = farthest(1) # B찾기
    print(farthest(edge)[1])
"""
N = int(input())
tree = {}
for _ in range(N):
    data = list(map(int, input().split()))
    tree[data[0]] = []
    for i in range(1, len(data) - 1, 2):
        tree[data[0]].append((data[i], data[i + 1]))

node, dist = farthest(1)
print(str(farthest(node)[1]))
"""

"""
# self함수는 해당 객체를 바꿈
a = []
b = [2]
a.append(b)
b.append(3)
print(a)
"""

