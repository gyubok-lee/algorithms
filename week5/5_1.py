# https://programmers.co.kr/learn/courses/30/lessons/72412

# ------------(내 풀이)-------------------
# 시간초과로 효율성 테스트 통과x

def mk_chart(info) :
    db = []
    for i in info:
        row = i.split()
        row[-1] = int(row[-1])
        db.append(row)
    return db

def find_query(db,query):
    res = []
    for q in query :
        cnt = 0
        tmp = q.split(' and ')
        line = tmp[:-1] + tmp[-1].split()

        for data in db:
            sw = True
            for col in range(4):
                if line[col] == '-' :
                    continue
                elif line[col] != data[col] :
                    sw = False
                    break
            if sw == True and int(line[4]) <= data[4] :
                cnt += 1

        res.append(cnt)
    return res

def solution1(info, query):
    database = mk_chart(info)
    return find_query(database,query)

# ------------(모범풀이)-------------------
# 모든 경우의 수를 딕셔너리로 저장, 이분탐색으로 갯수 탐색

from itertools import combinations

def mk_database(cond, score):
    for n in range(5):
        comb = list(combinations(range(4), n))
        for c in comb:
            t_c = cond.copy()
            for v in c:
                t_c[v] = '-'
            changed_t_c = '/'.join(t_c)
            db.setdefault(changed_t_c,[])
            db[changed_t_c].append(score)
    return

def query_finder (query):
    answer = []
    for q in query:
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:  # 딕셔너리 내에 값이 존재한다면,
            data = db[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data)  # lower bound 알고리즘
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)  # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)
    return answer

def solution(info, query):
    global db
    db = {}
    answer = []
    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        mk_database(conditions, score)
    for value in db.values():
        value.sort()
    return query_finder (query)


info_ = ["java backend junior pizza 150",
         "python frontend senior chicken 210",
         "python frontend senior chicken 150",
         "cpp backend senior pizza 260",
         "java backend junior chicken 80",
         "python backend senior chicken 50"]

query_ = ["java and backend and junior and pizza 100",
          "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150",
          "- and - and - and chicken 100",
          "- and - and - and - 150"]

print(solution(info_,query_))
