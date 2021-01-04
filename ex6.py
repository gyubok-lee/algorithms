# https://www.acmicpc.net/problem/13305

num = int(input())
dist = list(map(int,input().split()))
cities = list(map(int,input().split()))

mx = cities[0]
ans = 0

for i in range(num-1):
    if mx > cities[i]:
        mx = cities[i]
    ans += mx*dist[i]
print(ans)