from typing import Optional
from lab7.vertex import Vertex


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]
