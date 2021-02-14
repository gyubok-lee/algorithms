# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    new_id = new_id.lower() # 1단계
    answer = ''

    for s in new_id : # 2단계
        if s.isalnum() :
            answer = answer + s
        elif s == '-' or s == '_':
            answer = answer + s
        elif s == '.' : # 3단계
            if len(answer) > 0 and answer[-1] != '.':
                answer = answer + s

    if len(answer) > 0 and answer[-1] == '.' : # 4단계
        answer = answer[:-1]

    if len(answer) == 0: # 5단계
        answer = 'a'

    if len(answer) >= 16: # 6단계
        answer = answer[:15]
        if answer[-1] == '.' :
            answer = answer[:-1]

    if len(answer) <= 2: # 7단계
        answer = (answer + answer[-1]*2)[:3]
    return answer

idx = "=.="
print(solution(idx))
