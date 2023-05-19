g = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}

v = []

def dfs(graph,start):
    v.append(start)
    # print(start,end=" ") in case u want to print without the "->" nonsense, uncomment this and remove lines 20,21,22 (last 3)
    for node in graph[start]:
        if node not in v:
            dfs(graph,node)

dfs(g,'A')
finalv=[i+"->" for i in v[0:-1]]
finalv.append(v[-1])
for j in finalv: print(j,end='')
