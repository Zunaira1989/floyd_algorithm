import sys

INF = sys.maxsize
GRAPH = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]
   
def floyd_warshall_iterative(graph
                             ):
    # Number of vertices in the graph
    n = len(graph)
    
    # Initialize the distance matrix with the given graph
    distance = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            distance[i][j] = graph[i][j]
    
    # Iterate through intermediate vertices
    for k in range(n):
        # Iterate through source vertices
        for i in range(n):
            # Iterate through destination vertices
            for j in range(n):
                # Update the distance if a shorter path is found
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

   
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
 
 
if __name__ == '__main__':
    print(GRAPH)
    floyd_warshall_recursive(GRAPH,0,0,0)
    print(GRAPH)