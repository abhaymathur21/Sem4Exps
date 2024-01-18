#from sys import maxsize
from itertools import permutations

# matrix representation of graph
graph = [[0, 10, 15, 20], 
   [10, 0, 35, 25],
   [15, 35, 0, 30], 
    [20, 25, 30, 0]]
s = 0 #source node
V = 4 #no. of vertices

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = 9999
    next_permutation=permutations(vertex)
    for i in next_permutation:
        # store current Path weight(cost)
        curr_pathwt = 0
        # compute current path weight
        k = s
        for j in i:
            curr_pathwt += graph[k][j]
            k = j
        curr_pathwt += graph[k][s]

        # update minimum
        min_path = min(min_path, curr_pathwt)        
    return min_path
  
print(travellingSalesmanProblem(graph, s))
