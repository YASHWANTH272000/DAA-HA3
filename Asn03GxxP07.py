import sys

# Distance give's the distance between source and the current vertice.
# Visited give's the covered nodes.
class Graph:

    # Creating a graph with no edges and with size no of vertices.
    def __init__(self, size):
        self.noVertices = size
        self.graph = [ [0]*self.noVertices for x in range(self.noVertices) ]

    # Setting up the graph.
    def setGraph(self, edges):
        for x in edges:
            self.graph[x[0]][x[1]] = x[2]

    # Setting up the vertex cost.
    def setVertex(self, vertex, start):
        self.mark = False
        self.costVertex = [0 for i in range(self.noVertices)]
        for x in vertex:
            self.costVertex[x[0]] = x[1]
            if x[0] == start:
                self.mark = True

    # Get's the next vertice which is not there in connected to the source.
    def getnextmin(self):

        # Setting the largest distance equal to infinity initialy
        min = sys.maxsize

        for v in range(self.noVertices):
            if self.dist[v] < min and self.visited[v] == False:
                min = self.dist[v]
                CurrVertex = v
        return CurrVertex

    def dijkstra(self, start):

        # Setting the distance from the source to all nodes equal to infinite.
        self.dist = [sys.maxsize] * self.noVertices

        # Setting the distance form source to source equal to zero.
        if self.mark == True:
            self.dist[start] = self.costVertex[start]
        else:
            self.dist[start] = 0

        # Setting all the vertices as non-visited.
        self.visited = [False] * self.noVertices

        for v in range(self.noVertices):
            # Checking the smallest distance from the current edges.
            u = self.getnextmin()
            self.visited[u] = True

            for v in range(self.noVertices):
                if self.graph[u][v] > 0 and self.visited[v] == False and \
                    self.dist[v] > self.dist[u] + self.graph[u][v]\
                    + self.costVertex[v]:
                    self.dist[v] = self.dist[u] + \
                    self.graph[u][v] + self.costVertex[v]

        self.printDistances()

    # Displaying distance between the source and other vertices.
    def printDistances(self):
        for v in range(self.noVertices):
            print("{0} is at a distance of {1}".format(v,self.dist[v]))

    # Displaying graph Contents.
    def displayGraph(self):
        for i in range(self.noVertices):
            print(self.graph[i])

filename = ""
try:
    filename =  sys.argv[1]
except:
    print("Enter file name ::")
    exit(0)
try:
    file = open(filename, "r")
except:
    print("File not present")
    exit(0)
try:
    temp = file.readline()
    n, m = map(int,temp.split())

    costVertex = []
    for i in range(n):
        temp = file.readline()
        v, c = map(int,temp.split())
        costVertex.append([v,c])

    costEdge = []
    for j in range(m):
        temp = file.readline()
        u, v, c = map(int,temp.split())
        costEdge.append([u,v,c])

    print("Enter the source vertex")
    source = int(input())
except:
    print("Input structure not proper")
    exit(0)
size = n
g = Graph(n)
g.setGraph(costEdge)
g.setVertex(costVertex, source)
g.dijkstra(source);
