# https://www.acmicpc.net/problem/9184
# 메모이제이션: 한번 값을 알아내면 그 값을 저장하라!

arr = [[[0]*21 for i in range(21)] for _ in range(21)]

def w(a,b,c):
    global arr

    if a<=0 or b <=0 or c<=0:
        return 1
    if a> 20 or b> 20 or c> 20:
        return w(20,20,20)
    if arr[a][b][c]:
        return arr[a][b][c]
    if a<b<c:
        arr[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return arr[a][b][c]

    arr[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return arr[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
