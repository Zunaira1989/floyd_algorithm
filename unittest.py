import unittest
import Floyds

class TestFloydRecursive(unittest.Testcase):
    
    def test_FloydRecursive(self): # unit test for recursive function
        #create a simple input graph 
        Graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]
            
        #Expected output after runing the floydWarshall algorithm
        expected_output = [
            [0,7,12,8]
            [INF, 0 , 5 , 7],
            [INF, INF, 0, 2]
            [INF,INF,INF,0]]
        
        #run the floydWarshall algorithm on the input graph
        result = Floyds.FloydRecursive(Graph,0)
        
        self.assertEqual(result, expected_output)
    
        