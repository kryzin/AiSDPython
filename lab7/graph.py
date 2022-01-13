from typing import Dict, List, Any, Optional, Callable
from enum import Enum
import networkx as nx

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]  # node and list of its connections

    def create_vetrex(self, data: Any) -> Vertex:
        new_vertex = Vertex(data)
        self.adjacencies[new_vertex] = data
        return new_vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):

        def create_edge(self, value, weight: Optional[float] = None):
            self.index[value] = weight

        self.adjacencies(source).create_edge(self.adjacencies(destination), weight)
        self.adjacencies(destination).create_edge(self.adjacencies(source), weight)

        # add to edge list

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:

        def create_edge(self, value, weight: Optional[float] = None):
            self.index[value] = weight

        self.adjacencies(source).create_edge(self.adjacencies(destination), weight)
        self.adjacencies(destination).create_edge(self.adjacencies(source), weight)
    #
    # def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
    #
    # def traverse_depth_first(self, visit: Callable[[Any], None]):
    #
    # def show(self):
    #
    # def print(self):


