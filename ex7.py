# https://www.acmicpc.net/problem/17298
# 스택
n = int(input())
arr = list(map(int,input().split()))
ans = [-1 for _ in range(n)]
stack = [0]
idx = 1

while stack and idx < n:
    while stack and arr[stack[-1]] < arr[idx]:
        ans[stack[-1]] = arr[idx]
        stack.pop()
    stack.append(idx)
    idx +=1

ans = list(map(str,ans))
print(" ".join(ans))
