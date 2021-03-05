# https://programmers.co.kr/learn/courses/30/lessons/64062

# 최적값을 찾는 가장 빠른 방법은 이분탐색임.
def check(stones, k, mid):
    cnt = 0
    for stone in stones:
        if (stone < mid):
            cnt += 1
        else:  # 연속으로 나온다면 아니면 다시 0으로
            cnt = 0
        if (cnt >= k):
            return False
    return True

def solution(stones, k):
    answer = 0
    left = 0
    right = max(stones)

    while left <= right :
        mid = (left + right) // 2
        if check(stones, k, mid):
            if answer < mid:
                answer = mid
            left = mid +1
        else:
            right = mid -1
    return answer

s = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
kk = 3
print(solution(s,kk))
