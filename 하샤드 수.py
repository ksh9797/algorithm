def solution(x):
    answer = True
    test=list(map(int,str(x)))
    test2 = 0
    print([int(a) for a in str(x)])
    for i in range(len(str(x))):
        test2+=[int(a) for a in str(x)][i]
    print(sum([int(a) for a in str(x)])) 
    print(test2)

    return x%test2==0

print(solution(13))