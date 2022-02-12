def solution(phone_number):
    answer = ''
    print(len(phone_number[:-4]))
    phone_number.replace(phone_number[:-4],'*')
    print(phone_number)
    

    anwer= "*"*len(phone_number[:-4])+phone_number[-4:]
    print(anwer)
    return answer


solution("01033334444")