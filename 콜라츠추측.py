def solution(num):
    answer = 0
    test= num
    for i in range(0,500):
        
        if(test==1):break
        if(test%2==0):
            answer+=1
            test=test/2
        else:
            answer+=1
            test=test*3+1
       
     
    return answer if answer<500 else -1

print(solution(1))