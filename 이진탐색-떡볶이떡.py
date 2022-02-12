n = 4# 떡의 개수
m= 6 # 떡의 길이
array =[19,15,10,17
] # 떡의 높이

start=0 # 시작점 
end = max(array) # 끝점

result = 0
while (start<=end):
    total=0
    mid =(start+end)//2
    for x in array:
        if x>mid:
            total+=x-mid
    if total<m:
        end=mid-1
    else:
        result = mid
        start=mid+1

print(result)