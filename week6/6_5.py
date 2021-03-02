# https://programmers.co.kr/learn/courses/30/lessons/64064

def dfs(cand,ids,ban,depth,visit):
    global res

    if depth == len(ban):
        sw = True
        for i in res : # 기존 명단과 완전히 겹치는지 판단
            if len(cand-i) == 0:
                sw= False
        if sw == True :
            res.append({i for i in cand})
        return

    for id in ids :
        sw = True
        if len(id) != len(ban[depth]):
            continue

        for i in range(len(id)): # 문자열 체크
            if ban[depth][i] != '*':
                if ban[depth][i] != id[i] :
                    sw = False
                    break

        if sw == True and id not in visit:
            cand.add(id)
            visit.append(id)
            dfs(cand,ids,ban,depth+1,visit)
            cand.remove(id)
            visit.pop()

def solution(user_id, banned_id):
    global res
    res = [set()] # 최초 비교를 위해 하나는 있어야함
    dfs(set(),user_id,banned_id,0,[])
    return len(res[1:])


u_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b_id = ["fr*d*", "abc1**"]
print(solution(u_id,b_id))