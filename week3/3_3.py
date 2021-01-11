# 여행경로

# 백트레킹을 활용한 dfs가 너무 약함. 다시 공부할것.
# 마킹에 대한 개념도 부실.
ans = []
def DFS(stack,res,track):

    if len(res) == n:
        ans.append(res[:])
        return ans

    while stack :
        now = stack.pop()
        if now not in routes :
            stack.append(now)
            return
        else:
            for i in routes[now]:
                if (now,i) not in track :
                    stack.append(i)
                    track.add((now,i))
                    res.append(i)
                    DFS(stack,res,track)
                    #track.remove((now,i))
                    #res.pop()

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
        routes[i].sort()

    s = ['ICN']
    ans = []
    track = set(())

    DFS(s,['ICN'],track)


    return ans[0]

t= [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
t1 = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
print(solution(t1))