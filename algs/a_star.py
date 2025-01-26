from planner import Planner
from coverage_path import CoveragePath
import heapq

class AStar(Planner):
    def __init__(self, field):
        super().__init__(field)

    def _heuristic(self, n1: tuple, n2: tuple):
        """
        Private function representing heuristic h(n) function for
        estimating cost to travel to neighbor. In this implementation,
        Manhattan distance is used, although several other options exist
        (see https://ics.uci.edu/~kkask/Fall-2016%20CS271/slides/03-InformedHeuristicSearch.pdf).
        """
        x1,y1=n1
        x2,y2=n2

        return abs(x1-x2) + abs(y1-y2)

    
    def plan(self):
        path=CoveragePath()
        pq=[] # priority queue
        heapq.heappush(pq, (0, self.field.start))
        visited = set()
        visited.add(self.field.start)
        path.add_node(self.field.start)

        while pq:
            _, node = heapq.heappop(pq)
            for neighbor in self.field.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.add_node(neighbor)
                    priority = 1 + self._heuristic(node, neighbor) # can add a custom cost here
                    heapq.heappush(pq, (priority, neighbor))
        return path
