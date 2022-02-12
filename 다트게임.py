def solution(dartResult):
    test= [i.isdigit() for i in dartResult]
    test2= [ ]
    i=0
    print(len(test))
    while(i<len(test)):
        if(test[i]==True):
            if(test[i+1]==True):
                test2.append(i)
                i=i+1
                print(i)
            else:
                test2.append(i)
        i=i+1
        print(i)
    print(test2)
    # for i in range(len(test)):
        
    #     if(test[i]==True):
    #         if(test[i+1]==True):
    #             print('temp')
    #             print(temp)
                
    #             #test2.append(te)
    #         test2.append(i)
    #     print(test2)
    
    exp=1
    count_list=[]
    print(test2)
    for i in range(3):
        if(i<2):
            result = dartResult[test2[i]:test2[i+1]]
        else:
            result= dartResult[test2[2]:]
            
        # 점수(value)
        value=0
        bonus_index=0
        option_index=0
        if(result[1].isdigit()==True):
            value=result[0:2]
            bonus_index=2
            option_index=3
        else:
            value=result[0]
            bonus_index=1
            option_index=2
        
         # 보너스 계산
        if(result[bonus_index]=='S'):
            exp=1   
        elif(result[bonus_index]=='D'):
            exp=2
        elif(result[bonus_index]=='T'):
            exp=3
        count= int(value)**exp
        # 길이가 3일때 - 옵션
       
        if((result[1].isdigit()==True and len(result)==4) or (result[1].isdigit()==False and len(result)==3)):
            if(result[option_index]=='*'):
                count*=2
                if(i>0):
                    count_list[i-1]=count_list[i-1]*2
            elif(result[option_index]=='#'):
                count*=-1
        count_list.append(count)
        print(count_list)
    return sum(count_list)

solution('10D4S10D')