# https://www.acmicpc.net/problem/15686

# 찾으려는 거리나 좌표가 명확한 경우 bfs는 필요없다.

from itertools import combinations

def find_chickens(m) : # 모든 조합 찾기
    res = 1e6
    comb = list(combinations(chicken,m))
    for i in comb:
        dist = cal_dist(i)
        if res > dist :
            res = dist
    return res

def cal_dist(ch) : # 거리 계산
    total_dist = 0
    for house in houses :
        x ,y = house[0], house[1]
        total_dist += min([abs(x-i[0]) + abs(y-i[1]) for i in ch])
    return total_dist

N, M = map(int,input().split())
houses = []
chicken = []
city = []

for i in range(N):
    row = list(map(int,input().split()))
    city.append(row)
    for j in range(len(row)) :
        if row[j] == 1 :
            houses.append((i,j))
        elif row[j] == 2:
            chicken.append((i, j))
print(find_chickens(M))