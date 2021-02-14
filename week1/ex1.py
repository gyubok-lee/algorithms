# https://programmers.co.kr/skill_checks/227014/result?first_passed=true

def solution(s):
    s = s[1:-1]
    s = s.replace("{", "$").replace("}", "$")
    a = s.split("$")

    m = []
    for i in a:
        if (i !="") and (i != ","):
                m.append(list(map(int,i.split(","))))
    m.sort(key = lambda x: len(x))
    res = []
    for i in m:
        for j in i:
            if j not in res:
                res.append(j)
    return res

ss = "{{20,111},{111}}"
print(solution(ss))