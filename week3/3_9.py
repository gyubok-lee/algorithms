# https://www.acmicpc.net/problem/10830

def dot_matrix(A, B):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = sum([A[i][k] * B[k][j] % 1000 for k in range(n)]) % 1000
    return result

def get_matrix(m,power):

    if power == 1:
        return m

    if power%2 == 0:
        mm = get_matrix(m,power//2)
        return dot_matrix(mm,mm)
    else :
        return dot_matrix(get_matrix(m,power-1),m)


n, power = map(int,input().split())
matrix = [list(map(int,input().split())) for i in range(n)]

ans = get_matrix(matrix,power)

for i in ans:
    print(' '.join(list(map(lambda x: str(x % 1000), i))))
