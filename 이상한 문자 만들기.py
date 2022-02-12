def solution(s):
    list = [];
    for i in s.split(" "):
        temp=''
        for j in range(len(i)):
            if(j%2==0):
                temp+=i[j].upper()

            else:
                temp+=i[j].lower()

        list.append(temp)
    return ' '.join(list)
print(solution("try hello world"))