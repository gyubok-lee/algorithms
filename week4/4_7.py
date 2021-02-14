# 백트레킹 -> 모든 조합 구하기

# 공통점: 중복된걸 찾지 않음
# 차이점: 조합의 경우 자신 이후에 대해서만 탐색

def permutation(depth,res,count) :
    if depth == count :
        print(res)

    for i in lst :
        if i not in res:
            res.append(i)
            permutation(depth+1,res,count)
            res.pop()

def combination(depth,res,count,start) :
    if depth == count :
        print(res)

    for i in range(start,len(lst)) :
        if lst[i] not in res:
            res.append(lst[i])
            combination(depth+1,res,count,i)
            res.pop()

lst = ['a','b','c','d','e']

print("\n순열")
permutation(0,[],3)
print("\n조합")
combination(0,[],3,0)
