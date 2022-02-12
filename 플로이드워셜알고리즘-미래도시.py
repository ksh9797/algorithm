from dis import dis


INF =int(1e9)
n=5 # 노드
m=7 #간선
graph = [[INF]*(n+1) for _ in range(n+1)]
print(graph)
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 간선 정보 추가
m_info  = [[1,2],[1,3],[1,4],[2,4],[3,4],[3,5],[4,5]]
for i in m_info:
    a,b = map(int,i)
    graph[a][b]=1
    graph[b][a]=1

k=5 # 거쳐가는곳
print(graph)
for node in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]= min(graph[a][b],graph[a][node]+graph[node][b])
distance = graph[1][k]+graph[k][4]
if (distance==INF):
    print(-1)
else:
    print(distance)
