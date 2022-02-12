
def eratosthenes(N):

    number_list = [ i for i in range(2,N+1)]

    for i in number_list:
        for j in number_list:
            if(j!=i and j%i==0):
                number_list.remove(j)
    return number_list


# 다른거

import math
n=100
array = [True for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):
    if array[i]==True:
        j=2
        while i*j<=n:
            array[i*j]=False
            j+=1

for i in range(2,n+1):
    if(array[i]):
        print(i)