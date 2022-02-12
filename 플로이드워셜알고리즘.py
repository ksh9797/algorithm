INF =int(1e9)
n=int(input()) # 노드
m=int(input()) #간선
graph = [[INF]*(n+1) for _ in range(n+1)]
print(graph)
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 간선 정보 추가
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b]=c


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1+n+1):
            graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])

print(graph)
