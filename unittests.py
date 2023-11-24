import unittest
import FloydRecursive


class TestFloydRecursive(unittest.TestCase):
    
    def test_FloydRecursive(self): # unit test for recursive function
        #create a simple input graph 
        
        INF = 99999
        
        Graph = [[0, 7, INF, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]]
            
        #Expected output after runing the floydWarshall algorithm
        expected_output = [[0,7,12,8],
        [INF, 0 , 5 , 7],
        [INF, INF, 0, 2],
        [INF,INF,INF,0]]
        
        #run the floydWarshall algorithm on the input graph
        FloydRecursive.floyd_warshall_recursive(Graph,0,0,0)
        print("Graph:")
        print(Graph)
        print("Expected Output:")
        print(expected_output)
        
        self.assertEqual(Graph, expected_output)
    
if __name__ == '__main__':
    unittest.main()