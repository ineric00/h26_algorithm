import sys
input = sys.stdin.readline

# 정점(컴퓨터) 수와 간선(연결선) 수 입력
n = int(input())
m = int(input())

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
count = 0

def dfs(node):
    global count
    visited[node] = True
    
    for adj in graph[node]:
        if not visited[adj]:
            count += 1 # 새롭게 감염되는 컴퓨터 수 증가
            dfs(adj)

# 1번 컴퓨터부터 시작
dfs(1)
print(count)
