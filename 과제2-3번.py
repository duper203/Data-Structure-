class Graph():
   INF = 999999
   def __init__(self, num_vertices):
       self.V = num_vertices
       self.graph = [[0 for column in range(num_vertices)] for row in range(num_vertices)]

   def printMST(self, parent):
       print("Edge     Weight")
       for i in range(1, self.V):
           print(f"{parent[i]+1} - {i+1}       {self.graph[i][parent[i]]}")


   def minKey(self, key, mstSet): #인접 리스트 중 최소 간선 찾기
       min = self.INF
       for v in range(self.V):
           if key[v] < min and mstSet[v] == False:
               min = key[v]
               min_index = v
       return min_index


   def prims(self): #프림 알고리즘
       key = [self.INF for _ in range(self.V)]

       parent = [None for _ in range(self.V)]

       key[0] = 0

       mstSet = [False for _ in range(self.V)]

       parent[0] = -1

       for _ in range(self.V):
           u = self.minKey(key, mstSet)
           mstSet[u] = True

           for v in range(self.V):
               if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                   key[v] = self.graph[u][v]
                   parent[v] = u

       self.printMST(parent)


g = Graph(7)
g.graph = [[0,5,0,3,0,0,0],
           [5,0,0,0,0,10,0],
           [0,0,0,0,8,0,11],
           [3,0,0,0,6,7,0],
           [0,10,8,6,0,0,13],
           [0,0,0,7,0,0,15],
           [0,0,11,0,13,15,0]]

g.prims()