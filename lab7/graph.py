from typing import Dict, List, Any, Optional
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
    adjacencies: Dict[Vertex, List[Edge]]

    def create_vetrex(self, data: Any) -> Vertex:
        new_vertex = Vertex(data)
        self.Dict[data] = new_vertex
        return new_vertex

    def

