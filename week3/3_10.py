# https://www.acmicpc.net/problem/1654

def binary_search(left, right,target):
    global ans
    mid = (left + right)//2
    if left > right :
        return

    cnt = 0
    for i in data:
        tmp = i
        while tmp >= mid:
            tmp -= mid
            cnt += 1

    if cnt >= target:
        if mid > ans :
            ans = mid
            binary_search(mid+1,right,target)
    else :
        binary_search(left,mid-1,target)

K, N = map(int,input().split())
data = [int(input()) for i in range(K)]
left = 1
right = max(data)
mid = (left + right)//2
ans = 0
binary_search(left,right,N)
print(ans)