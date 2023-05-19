g = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}
v=[]
def BFS(graph,start):
  q=[]
  for node in graph[start]:
    q.append(node)

  v.append(start)
  print(end=start)
  for node in q:
    v.append(node)
    print("->",end=node)
    for i in graph[node]:
      q.append(i)
BFS(g,'A')