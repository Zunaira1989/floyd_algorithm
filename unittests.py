import sys 
# Defines the value of infinity 
NO_PATH = 999999999
Graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]

MAX_LENGTH = len(Graph[0])

def floyd (distance):
    size_of_graph = len(Graph)-1 # Calculates the size of the graph, -1 is used due to indexing starting at 0, the graph has 4 elements, thus the indexing starts from 0 , and goes up to 3. 
    
    # Recursive method of implementing Floyd Algorithm, using Loops 
    
    def recursive_floyd(i,j,k,Graph,size_of_graph):
        if i < size_of_graph:
            Graph[i][j] = min(Graph[i][j],Graph[i][k] + Graph[k][j]
            i+=1
            j=0 
            recursive_floyd(i,j,k,Graph,size_of_graph)
            if j < size_of_graph:
                Graph[i][j] = min(Graph[i][j],Graph[i][k] + Graph[k][j] 
                                  
                recursive_floyd(i,j,k,Graph,size_of_graph)                  
                if k < size_of_graph:
                # Update the shortest path if a shorter path is found
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                    floyd_warshall_recursive(i, j, k + 1, graph, size_of_graph)
                else:
                    floyd_warshall_recursive(i, j + 1, 0, graph, size_of_graph)
            else:
                    floyd_warshall_recursive(i + 1, 0, 0, graph, size_of_graph)

    
    print(Graph)
    
        
    