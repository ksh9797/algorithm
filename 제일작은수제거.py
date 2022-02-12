arr=[10,3,1,2]
print(len(arr))
print(min(arr))
test=min(arr)
print(test)
print(arr.remove(10))

def solution(arr):
    answer = []
    if(len(arr)==1):
        return [-1]
    a = min(arr)
    for i in arr:
        if(i!=a):
            answer.append(i)
    return answer

def solution(arr):
    answer = []
    if(len(arr)==1):
        return [-1]
    a = min(arr)
    arr.remove(min(arr))
    return arr

print(solution([4,3,2,1]))