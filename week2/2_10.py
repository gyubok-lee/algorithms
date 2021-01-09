def solution(str1, str2):
    set1 = []
    set2 = []
    total = dict()

    str1 = str1.lower()
    str2 = str2.lower()

    for i in range(len(str1)-1) :
        if str1[i].isalpha() and str1[i+1].isalpha() :
            set1.append(str1[i] + str1[i+1])
            total.setdefault(str1[i] + str1[i+1],[0,0])
            total[str1[i] + str1[i+1]][0] += 1

    for i in range(len(str2)-1) :
        if str2[i].isalpha() and str2[i+1].isalpha() :
            set2.append(str2[i] + str2[i+1])
            total.setdefault(str2[i] + str2[i + 1], [0, 0])
            total[str2[i] + str2[i + 1]][1] += 1

    intersect = 0
    union = 0
    for i in total :
        if total[i][0] != 0 and total[i][1] != 0 :
            union += max(total[i][0], total[i][1])
            intersect += min(total[i][0], total[i][1])
        else :
            union += max(total[i][0], total[i][1])

    ans = 0
    if union == 0:
        ans = 1
    else :
        ans = intersect/union
    ans = int(ans * 65536)
    return ans

s1 = 'E=M*C^2'
s2 = 'e=m*c^2'
print(solution(s1,s2))

