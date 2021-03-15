# https://programmers.co.kr/learn/courses/30/lessons/17678

from collections import deque

def str2int(s):
    time = s.split(":")
    return int(time[0]) * 60 + int(time[1])

def int2str(i):
    hour = str(i // 60)
    minute = str(i % 60)
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    return hour + ':' + minute

def solution(n, t, m, timetable):
    shuttle = deque([i*t + 540 for i in range(n)])
    arrive_que = []
    ans = 0
    for i in timetable :
        arrive_que.append(str2int(i))
    arrive_que = deque(sorted(arrive_que))

    while shuttle:
        now = shuttle.popleft()
        cnt = 0

        if len(shuttle)== 0 : # 마지막 버스
            if len(arrive_que) < m: # 줄이 작은 경우
                ans = now
            else : # 줄이 큰 경우
                ans = min(now,arrive_que[m-1] -1)
        else :
            while cnt < m  :
                if arrive_que[0] <= now :
                    cnt += 1
                else:
                    break
    return int2str(ans)

n = 1
t = 1
m = 1
tt = ["23:59"]
print(solution(n,t,m,tt))