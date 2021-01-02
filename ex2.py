# 프로그래머스- 입국심사
# 이분탐색 알고리즘

def solution(n, times):
    right = min(times) * n
    left = 1
    answer = 0
    while(left <= right):
        mid = (right + left) // 2
        temp = n
        print("mid = ", mid, "left= ",left, "right = ",right)
        for i in times:
            temp -= mid//i
            print(i, temp)
            if temp <= 0:
                answer = mid
                right = mid - 1
                break
        if temp > 0:
            left = mid + 1
    return answer

nn  =6
tm = [7,10]
print(solution(nn,tm))