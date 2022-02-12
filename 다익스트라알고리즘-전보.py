import heapq
INF = int(1e9)
n,m = map (int ,[3,2])
start = 1
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
info = [[1,2,4],[1,3,2]]
for i in info:
    a,b,c = map (int , i)
    graph[a].append((b,c))

def dijkstra(start):
    q= [ ]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if (distance[now] <dist):
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if(cost<distance[i[0]]):
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
count = 0
max_distance= 0
for d in distance :
    if d != INF:
        count+=1
        max_distance=max(max_distance,d)
# count-1 하는 이유 : 시작 노드 제외
print(count-1,max_distance)