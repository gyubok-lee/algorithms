# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3

# 해당 단계는 이전 단계들의 조합으로 이루어진다.
# 3 = 1+2 / 4 = 1+3, 2+2 / 5 = 1+4, 2+3 / ....

def solution(N, number):
    if N == number :
        return 1
    res = [0, {N}]
    for i in range(2, 9): # 각 단계
        case_set = {int(str(N)*i)} # 이어서 붙인 수(따로)

        for i_half in range(1, i//2+1): # 이전 단계들의 조합
            for x in res[i_half]:
                for y in res[i-i_half]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y//x)
                    if y != 0:
                        case_set.add(x//y)
        if number in case_set:
            return i
        res.append(case_set)
    return -1


print(solution(5, 5))