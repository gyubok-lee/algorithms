# 이진탐색, lower_bound

def lower_bound(start,end,target) :# lower bound 알고리즘
    while start != end and start != len(lst):
        if lst[(start + end) // 2] >= target:
            end = (start + end) // 2
        else:
            start = (start + end) // 2 + 1
    return start

def binary_search(start, end,target):
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return start
lst = [i+1 for i in range(10)]
print(lst)

print(lower_bound(0,len(lst),6))
print(binary_search(0,len(lst),6))