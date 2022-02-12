def solution(n, m):
    answer = [1];
    n_list=[];
    m_list=[];
    tempn=n
    tempm=m
    while(n!=1):
        for i in range(1,n+1):
            if(n%i==0):
                n_list.append(i);

                
           
    while(m!=1):
        for i in range(1,m+1):
            if(m%i==0):
                m_list.append(i);
    print(n_list)
    print(m_list)
    
    # 두 리스트가 모두 가진 수 (겹치는 원소 = 교집합)( 최대 공약수)
    print(list(set(n_list) & set(m_list)))

    for i in list(set(n_list) & set(m_list)):
        answer[0]*=i
    # for i in list(set(n_list) | set(m_list)):
    #     answer[1]*=i

    # 최소공배수 -> 최대공약수로 나눈 후 몫 곱하기..
    print(answer[0])
    print()
    print(tempn//answer[0]*tempm//answer[0]*answer[0])
    answer.append(tempn//answer[0]*tempm//answer[0]*answer[0])
    print(tempm//answer[0])
    print(list(set(n_list) | set(m_list)))
    cnt = [(i+1)*m_list.count(i) for i in n_list if m_list.count(i) > 1]
    print(cnt)
    # 두 리스트 중복 제거 후 곱하기  합집합 (최소 공배수)


    print(answer)
    return answer
print("test")
# solution(3,300);
# 3=1*3
# 12 = 1*2*3*2

# 유클리드 호제법
def solution2(n,m):
    # m과 n중 큰 수 구하기
    answer=[1,1]
    if(n>m):
        max=n
        min=m
    elif(m>n):
        max=m
        min=n
    else:
        answer=[n,n]
        return answer
    temp=min
    while (temp!=0):
        
        temp=max%min
        max=min
        min=temp
    answer[0]=max
    # 최대 공배수
    answer[1]=int(n*m/max)
    return answer

print(solution2(2,5))
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    print(c,d)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(4,4))