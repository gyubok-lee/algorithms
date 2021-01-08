# https://programmers.co.kr/learn/courses/30/lessons/60061

# 과도하게 어렵게 생각하는 경향이 있음. 최대한 단순화하고, 무식한 코드부터라도 짜기

# 현 상태가 가능한 상태인지를 판단
def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL:  # 기둥일 때
            if y != 0 and (x, y - 1, COL) not in result and \
                    (x - 1, y, ROW) not in result and (x, y, ROW) not in result:
                return True
        else:  # 보일 때
            if (x, y - 1, COL) not in result and (x + 1, y - 1, COL) not in result and \
                    not ((x - 1, y, ROW) in result and (x + 1, y, ROW) in result):
                return True
    return False


def solution(n, build_frame):
    result = set()

    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:  # 추가일 때
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result:  # 삭제할 때
            result.remove(item)
            if impossible(result):
                result.add(item)
    answer = map(list, result)

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))
bf = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(5,bf))