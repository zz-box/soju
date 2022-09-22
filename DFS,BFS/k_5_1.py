n, m = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

def function(x,y):
    if x <= -1 or x >= n  or y <= -1 or y>=m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        function[x-1][y]
        function[x+1][y]
        function[x][y-1]
        function[x][y+1]
        
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if function(n,m):
            result += 1

print(result)