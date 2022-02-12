import heapq
INF = int(1e9)
n,m = map (int ,[6,11])
start = 1
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
info = [[1,2,2],[1,4,1],[1,3,5],
[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]
for i in info:
    a,b,c = map (int , i)
    graph[a].append((b,c))
print(graph)

def dijkstra(start):
    q= [ ]
    heapq.heappush(q,(0,start))
    print(q)
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        print(dist,now)

        if (distance[now] <dist):
            continue
        for i in graph[now]:
            print("i")
            print(i) 
            cost = dist + i[1]
            if(cost<distance[i[0]]):
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                print(q)

dijkstra(start)
print(distance)
for i in range(1,n+1):
    if(distance[i])==INF:
        print("infinity")
    else:
        print(distance[i])