import time
def two_pointer(result, list):
    start_index=0
    end_index=0
    count=0
    while True:
        if(sum(list[start_index:end_index])==result):
            count+=1
        if (sum(list[start_index:end_index])<result):
            end_index+=1
        elif( sum(list[start_index:end_index])>=result):
            start_index+=1
        if (start_index ==len(list)):
            break
    return count
start = time.time()       
print(two_pointer(5,[1,2,3,2,5]))
end = time.time()
print(f"{end - start:.5f} sec")


# 2번째

def two_pointer2(result,list):
    count = 0 
    interval_sum=0
    end=0
    for start in range(result):
        while interval_sum<5 and end<result:
            interval_sum+=list[end]
            end+=1
        if interval_sum ==5:
            count+=1
        interval_sum -=list[start]
    return count

start = time.time()       
print(two_pointer2(5,[1,2,3,2,5]))
end = time.time()
print(f"{end - start:.5f} sec")
