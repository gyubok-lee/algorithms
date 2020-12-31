def get_time(s,t) :
    hh,mm,ss = map(float,s.split(":"))
    end = hh * 3600 + mm * 60 + ss
    ex = float(t[:-1])
    start = end -ex + 0.001
    return [start, end]

def counter(time , lst) :
    cnt = 0
    st = time
    end = time + 1
    for i in lst : # 1초 구간이 해당 작업시간 안에 있는가?
        if i[1] >= st and i[0] < end:
            cnt += 1
    return cnt

def solution(lines):
    schedule = []
    for line in lines :
        log = line.split()
        schedule.append(get_time(log[1],log[2]))
    res = 1
    for i in schedule :
        res = max(res,counter(i[0],schedule),counter(i[1],schedule))
    return res

l = 	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(l))