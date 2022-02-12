def solution(arr1, arr2):
    answer = [[0]*len(arr1[0]) for i in range(len(arr1))]
    print(answer)
    print(len(arr1[0])) # 열
    print(len(arr1)) # 행
    answer[0][0]=arr1[0][0]+arr2[0][0]
    answer[1][0]=arr1[1][0]+arr2[1][0]
    print(answer)
    return answer

solution([[1],[2]],[[3],[4]]) #2행 1열 (2*1)

def solution2(arr1, arr2):
    answer = [[0]*len(arr1[0]) for i in range(len(arr1))]
    print(answer)
    print(len(arr1[0])) # 열
    print(len(arr1)) # 행
    answer[0][0]=arr1[0][0]+arr2[0][0]
    answer[1][0]=arr1[1][0]+arr2[1][0]
    answer[0][1]=arr1[0][1]+arr2[0][1]
    answer[1][1]=arr1[1][1]+arr2[1][1]
    print(answer)
    return answer

solution2([[1,2],[2,3]]	,[[3,4],[5,6]]	) #2행 2열 (2*2)



def solution3(arr1, arr2):
    answer = [[0]*len(arr1[0]) for i in range(len(arr1))]
    print(answer)
    print(len(arr1[0])) # 열
    print(len(arr1)) # 행
    for i in range(len(arr1[0])): #0
        for j in range(len(arr1)): #0,1
            answer[j][i]=arr1[j][i]+arr2[j][i]
    print(answer)
    return answer

solution3([[1],[2]],[[3],[4]]	) 
solution3([[1,2,3],[2,3,4]]	,[[3,4,5],[5,6,7]]	)