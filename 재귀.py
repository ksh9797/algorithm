# 1. 팩토리얼
# n = int(input())

# def factorial(n):
#     if(n<1):
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(n))

#2 . 하노이탑
n=int(input())


def hanoi(n,start,end,mid):
    if(n==1):
        return print(start,end)
    hanoi(n-1,start,mid,end)
    print(start,end)
    hanoi(n-1,mid,end,start)

print(2**n-1)
hanoi(n,1,3,2)