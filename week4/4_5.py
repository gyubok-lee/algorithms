# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    arr = [[triangle[0][0]]]
    for i in range(1,len(triangle)) :
        row = triangle[i]
        for j in range(len(row)):
            if j == 0:
                row[j] =  arr[i-1][0] + row[j]
            elif j == len(row) - 1:
                row[j] = arr[i-1][-1] + row[j]
            else :
                row[j] = max(arr[i-1][j-1],arr[i-1][j]) + row[j]
        arr.append(row)

    return max(arr[-1])


t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(t))