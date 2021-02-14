# https://www.acmicpc.net/problem/15684

# dfs로 브루트포스 하는 알고리즘 능숙하게 짤 수 있도록 해야함.
from itertools import combinations

def add_ladder():
    for nselect in range(4):
        comb = combinations(cands,nselect) # 후보군 선택
        for c in comb:
            sw = True
            changed = []

            for a,b in c: # 이어서 붙이는 경우를 제외
                if (ladders[b][a] == 0) and (ladders[b+1][a] == 0):
                    ladders[b][a] = 1
                    ladders[b+1][a] = -1
                    changed.append((a,b))
                else :
                    sw = False
                    break

            if sw == True:
                if simulation(ladders) == True:
                    return nselect

            for a,b in changed : # 원상복구
                ladders[b][a] = 0
                ladders[b+1][a] = 0

    return -1

def simulation(ladders) :
    global N
    global H
    for i in range(1,N+1): # 시작 세로선
        x = i
        for j in range(1,H+1): # 맨 밑까지
            x += ladders[x][j]
        if x != i :
            return False
    return True

# main
N, M ,H = map(int,input().split())
cands = set([])
for i in range(1,H+1):
    for j in range(1,N):
        cands.add((i,j))

# 자료구조 초기화
ladders = dict()
for i in range(1, N + 1):
    ladders.setdefault(i, [0] * (H + 1))

# 가로선 입력
for i in range(M):
    a,b = map(int,input().split())
    ladders[b][a] = 1
    ladders[b + 1][a] = -1
    cands.remove((a,b))

print(add_ladder())
