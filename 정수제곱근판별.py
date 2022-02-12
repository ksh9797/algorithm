import math
# def solution(n):
#     is_integer= math.sqrt(n).is_integer()
#     print(is_integer)
#     if(is_integer): return int((math.sqrt(n)+1)**2)
#     else: return -1 


def solution(n):
    is_integer= (n**0.5).is_integer()
    print(is_integer)
    return int((n**0.5+1)**2) if is_integer else -1

print(solution(3))