# https://programmers.co.kr/learn/courses/30/lessons/60062

# 그리디인줄 알았으나 완전탐색에 대한 문제
# set을 활용한 탐색 방법에 대한 공부 필요

def solution(n, weak, dist):

    W, F = len(weak), len(dist)
    repair = [()] # 수리된 지점들
    cnt = 0
    dist.sort(reverse=True)

    # 고칠 수 있는 것들
    for workers in dist:
        work = []  # 각각 고칠 수 있는 취약점들
        cnt += 1

        # 수리 가능한 지점 찾기
        for i, j in enumerate(weak):
            start = j  # 각 위크포인트부터 시작
            ends = weak[i:] + [n+w for w in weak[:i]]  # 정방향으로 지점들 나열
            can = [end % n for end in ends if end -
                   start <= workers]  # 가능한 지점 저장
            work.append(set(can))

        # 수리 가능한 경우 탐색
        cand = set()
        for w in work:
            for x in repair:
                new = w | set(x)
                if len(new) == W:
                    return cnt
                cand.add(tuple(new))
        repair = cand

    return -1

n = 12
w = [1, 5, 6, 10]
d = [1, 2, 3, 4]
print(solution(n,w,d))