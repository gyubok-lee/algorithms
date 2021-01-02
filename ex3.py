# 프로그래머스 - 매칭점수(카카오 기출)
# 정확하게 문자열을 파싱하는 능력이 중요. 이후 자료구조를 짜는 것까지
# 정규표현식에 대해 잘 알아야함.

import re
def solution(word, pages):
    res = []
    target = word.lower()

    for page in pages:
        info = []

        # 제목찾기
        title = page.split("content=")[1].split(">")[0]
        info.append(title)

        # 기본점수
        cnt = 0
        html1 = re.sub("[^a-zA-Z]+", " ", page.lower().replace("\n"," ")).split()
        for _ in html1:
            if _ == target:
                cnt +=1
        info.append(cnt)

        # 외부링크 수
        html2 = page.split("<a href=")
        info.append(len(html2)-1)

        # 링크점수
        ll = []
        for _ in html2[1:]:
            linked = _.split(">")[0] +"/"
            ll.append(linked)
        info.append(ll)
        res.append(info)

    temp = dict()
    for page in res:
        for link in page[-1]:
            temp.setdefault(link,0)
            temp[link] += page[1]/page[2]


    # 매칭점수 계산
    ans = -1
    max_score = 0
    tt = []

    for i in range(len(res)):
        ls =0
        bs = float(res[i][1])
        fs = ls + bs
        if res[i][0] in temp :
            ls = temp[res[i][0]]
            fs = float(ls) + bs
        if max_score <= fs:
            ans = i
            max_score = fs
        tt.append([ls,fs])
    return ans

# 아래는 모범코드
import re
def solution(word, pages):
    urlToIdx = {}
    urlToScore = {}
    urlToExlink = {}
    word= word.lower()
    for i in range(len(pages)):
        lp = pages[i].lower()
        url = re.search(r'<meta[^>]*content="https://([\S]*)"/>',lp).group(1)
        urlToIdx[url] = i
        wordCnt = 0
        for find in re.findall(r'[a-zA-Z]+',lp): #영문자들만 골라 리스트로
            if find == word :
                wordCnt += 1
        s = set()
        for e in re.findall(r'<a href="https://[\S]*">',lp):
            s.add(re.search(r'"https://([\S]*)"',e).group(1))
        s = list(s)

        urlToScore[url] = list()
        urlToScore[url].append(wordCnt)
        urlToScore[url].append(len(s))

        for e in s:
            if e not in urlToExlink :
                urlToExlink[e] = list()
            urlToExlink[e].append(url)

    res = []
    for k,v in urlToScore.items():
        score = v[0]
        if k in urlToExlink:
            for u in urlToExlink[k]:
                score += urlToScore[u][0] / urlToScore[u][1]
        res.append([score, urlToIdx[k]])

    return sorted(res, key = lambda x: [-x[0],x[1]])[0][1]