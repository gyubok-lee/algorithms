# 여행경로

# 백트레킹을 활용한 dfs가 너무 약함. 다시 공부할것.
# 마킹에 대한 개념도 부실. 해야할때와 필요없을때를 알것

def DFS(stack,track):

    while len(stack) :
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            track.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return track[::-1]

def solution(tickets):
    global routes
    global n
    global ans

    n = len(tickets) + 1
    routes = dict()
    for f, t in tickets:
        routes.setdefault(f,[])
        routes[f].append(t)

    for i in routes :
        routes[i].sort(reverse = True)
    ans = DFS(['ICN'],[])

    return ans

t= [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
t1 = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
print(solution(t1))