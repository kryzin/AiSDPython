from project1 import Queue
from typing import Any

class Vertex:
    def __init__(self, data):
        self.data: Any

class Edge:
    def __init__(self, source, destination):
        self.source: Vertex
        self.destination: Vertex

class Graph:
    def __init__(self):
        self.graph = dict[Vertex, list(Edge)]

    def create_vertex(self, data):
        new_vertex = Vertex(data)
        self.graph[new_vertex] = ()

    def add_edge(self, src, dest):
        new_edge = Edge(src, dest)

        list_src = self.graph.get(src)
        list_src.append(dest)
        self.graph[src] = list_src

        list_dest = self.graph.get(dest)
        list_dest.append(src)
        self.graph[dest] = list_dest


    # def BFS(self, s):
    #
    #     # Mark all the vertices as not visited
    #     visited = [False] * (max(self.graph) + 1)
    #
    #     # Create a queue for BFS
    #     queue = []
    #
    #     # Mark the source node as
    #     # visited and enqueue it
    #     queue.append(s)
    #     visited[s] = True
    #
    #     while queue:
    #
    #         # Dequeue a vertex from
    #         # queue and print it
    #         s = queue.pop(0)
    #         print(s, end=" ")
    #
    #         # Get all adjacent vertices of the
    #         # dequeued vertex s. If a adjacent
    #         # has not been visited, then mark it
    #         # visited and enqueue it
    #         for i in self.graph[s]:
    #             if visited[i] == False:
    #                 queue.append(i)
    #                 visited[i] = True
    #
    # def DFSUtil(self, v, visited):
    #
    #     # Mark the current node as visited
    #     # and print it
    #     visited.add(v)
    #     print(v, end=' ')
    #
    #     # Recur for all the vertices
    #     # adjacent to this vertex
    #     for neighbour in self.graph[v]:
    #         if neighbour not in visited:
    #             self.DFSUtil(neighbour, visited)
    #
    # # The function to do DFS traversal. It uses
    # # recursive DFSUtil()
    # def DFS(self, v):
    #
    #     # Create a set to store visited vertices
    #     visited = set()
    #
    #     # Call the recursive helper function
    #     # to print DFS traversal
    #     self.DFSUtil(v, visited)
    #
    # def minDistance(self, dist, sptSet):
    #
    #     # Initialize minimum distance for next node
    #     min = sys.maxsize
    #
    #     # Search not nearest vertex not in the
    #     # shortest path tree
    #     for v in range(self.V):
    #         if dist[v] < min and sptSet[v] == False:
    #             min = dist[v]
    #             min_index = v
    #
    #     return min_index
    #
    # def printSolution(self, dist):
    #     print("Vertex tDistance from Source")
    #     for node in range(self.V):
    #         print(node, "t", dist[node])

# Driver program to the above graph class
graph = Graph
graph.create_vertex('VI')
graph.create_vertex('RU')
graph.add_edge('VI', 'RU')

# graph = Graph(V)
# graph.add_edge(0, 1)
# graph.add_edge(0, 4)
# graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(1, 4)
# graph.add_edge(2, 3)
# graph.add_edge(3, 4)

graph.print_graph()