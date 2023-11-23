import sys

INF = sys.maxsize
GRAPH = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]
   
def floyd_warshall_recursive(i,j,k):
    
    size_of_graph = len(GRAPH)-1

    if i < size_of_graph:
        if j < size_of_graph:
            if k < size_of_graph:
                GRAPH[i][j] = min(GRAPH[i][j], GRAPH[i][k] + GRAPH[k][j])
                floyd_warshall_recursive(i, j, k + 1)
            else:
                floyd_warshall_recursive(i, j + 1, 0)
        else:
            floyd_warshall_recursive(i + 1, 0, 0)

floyd_warshall_recursive(0, 0, 0)
print(GRAPH)

   
 