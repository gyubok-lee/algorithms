# https://programmers.co.kr/learn/courses/30/lessons/72414

# 동적계획법을 활용한 시청자수 마킹
def str2int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def int2str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    play_time = str2int(play_time)
    adv_time = str2int(adv_time)
    total_time = [0 for i in range(play_time + 1)]

    for l in logs:
        start, end = l.split('-')
        start = str2int(start)
        end = str2int(end)
        total_time[start] += 1
        total_time[end] -= 1

    # # 각 시간별 시청자 수
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]

    # 누적 시청 가중치 -> 시간이 길어질수록 가중치가 높아짐
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]

    # i <- 광고가 끝나는 시간
    most_view = total_time[adv_time - 1]
    max_time = 0
    for i in range(adv_time, play_time):
        if i >= adv_time:
            if most_view < total_time[i] - total_time[i - adv_time]:
                most_view = total_time[i] - total_time[i - adv_time]
                max_time = i - adv_time + 1

    return int2str(max_time)

pt = "02:03:55"
at = "00:14:15"
lgs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(pt,at,lgs))