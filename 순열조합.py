# itertools 라이브러리 활용
from itertools import permutations, combinations
# 순열
for i in permutations([1,2,3,4],2):
    print(i,end=" ")

# 조합
for i in combinations([1,2,3,4,5],2):
    print(i,end=" ")


# 직접 구현

# 조합
def combinations(arr,r):
    for i in range(len(arr)):
        if r==1:
            # yield => return과 비슷 그러나 generator 객체 만들어줌
            # 메모리 낭비 막음
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]]+next


# 순열
def permutation(arr,r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:],r-1):
                yield [arr[i]]+next

