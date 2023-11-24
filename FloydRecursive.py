import sys

INF = sys.maxsize
GRAPH = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]
   
def floyd_warshall_recursive(graph, i, j, k):
    size_of_graph = len(graph)

    if i < size_of_graph:
        if j < size_of_graph:
            if k < size_of_graph:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                floyd_warshall_recursive(graph, i, j, k + 1)
            else:
                floyd_warshall_recursive(graph, i, j + 1, 0)
        else:
            floyd_warshall_recursive(graph, i + 1, 0, 0)

   
 