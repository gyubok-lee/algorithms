# https://www.acmicpc.net/problem/16235

# 문제에서 주어진 조건을 빠짐없이 기록할것
def spring():
    dead = []
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) > 0:
                trees[i][j] = sorted(trees[i][j])
                for k in range(len(trees[i][j])):
                    if soil[i][j] < trees[i][j][k]:
                        for _ in range(k,len(trees[i][j])):
                            dead.append([i,j,trees[i][j][_]])
                        trees[i][j] = trees[i][j][:k]
                        break
                    else:
                        soil[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
    return dead

def summer(dead):
    for i in dead:
        soil[i[0]][i[1]] += i[2]//2
    return

def autumn() :
    deltas = [(-1,-1), (-1,0), (-1,1), (0,-1),
              (0,1), (1,-1), (1,0), (1,1)]
    growed = []

    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 ==0 and trees[i][j][k] >= 5:
                    growed.append((i,j))

    while growed :
        x,y = growed.pop()
        for d in deltas:
            nx, ny = x + d[0], y + d[1]
            if 0<=nx<N and 0<=ny<N :
                trees[nx][ny].append(1)
    return

def winter():
    for i in range(N):
        for j in range(N):
            soil[i][j] += feed[i][j]
    return

if __name__ == '__main__' :
    N,M,K = map(int,input().split())
    feed = [list(map(int, input().split())) for i in range(N)]
    soil = [[5]*N for i in range(N)]
    trees = [[[] for i in range(N)] for j in range(N)]
    for i in range(M):
        x,y,z = map(int,input().split())
        trees[x-1][y-1].append(z)

    for _ in range(K):
        dead_trees = spring()
        summer(dead_trees)
        autumn()
        winter()

    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += len(trees[i][j])
    print(cnt)
