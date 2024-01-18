import copy

initial = [[1,2,3],[-1,4,6],[7,5,8]]
temp = initial.copy()
goal = [[1,2,3],[4,5,6],[7,8,-1]]

def displaced(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != goal[i][j]:
                count += 1
    return count

def getAdjacent(matrix, i, j):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    adj = []
    for dx, dy in moves:
        ni, nj = i + dx, j + dy
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[ni]):
            adj.append(matrix[ni][nj])
    return adj

def printmatrix(matrix):
    for row in matrix:
        print(*row)

def swap(matrix, a, b):
    ai, aj, bi, bj = 0, 0, 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == a:
                ai, aj = i, j
            if matrix[i][j] == b:
                bi, bj = i, j
    matrix[ai][aj], matrix[bi][bj] = matrix[bi][bj], matrix[ai][aj]
    return matrix

def Astar(temp, gn):
    printmatrix(temp)
    i1, j1 = 0, 0
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == -1:
                i1, j1 = i, j
                break
    gn += 1
    vt = getAdjacent(temp, i1, j1)
    number_to_swap = min(vt, key=lambda x: displaced(swap(copy.deepcopy(temp), x, -1)))
    temp = swap(temp, number_to_swap, -1)
    #print("  |")
    print("  ↓")
    if temp == goal:
        print("THE GOAL STATE HAS BEEN REACHED")
    else:
        Astar(temp, gn)

Astar(temp, -1)

