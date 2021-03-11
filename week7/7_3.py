# https://www.acmicpc.net/problem/14890

def slope(road) :
    prev = road[0]
    order = 1
    cnt = 1 # 같은 칸이 연속으로 이어지는 횟수
    placed = [0] * len(road) # 경사로를 놓은 곳

    while order < len(road):
        now = road[order]

        if now == prev : # 높이가 같다면
            cnt +=1

        elif now > prev : # 높아졌다면
            if now - prev > 1:
                return False
            else : # 낮은 높이가 L이상 연속나왔었는지
                if cnt < L :
                    return False
            for _ in range(order-L,order):
                if placed[_] != 0:
                    return False
                placed[_] = 1
            cnt = 1

        elif now < prev: # 낮아졌다면
            if prev - now > 1:
                return False
            else: # 낮은 높이가 앞으로 L이상 이어지는지
                for i in range(order,order + L):
                    if i >= len(road) :
                        return False
                    if road[i] != now :
                        return False

                # 불필요한 반복을 피하기 위해 인덱스를 미리 땡김
                for _ in range(order, order+L):
                    if placed[_] != 0:
                        return False
                    placed[_] = 1

                prev = road[order + L -1]
                order += L
                continue

            cnt = 1
        prev = now
        order += 1
    return True


if __name__ == '__main__' :
    N, L = map(int,input().split())
    roads = [list(map(int,input().split())) for i in range(N)]
    ans = 0

    for i in range(N):
        if slope(roads[i]) :
            ans += 1
        if slope([roads[_][i] for _ in range(N)]):
            ans += 1
    print(ans)