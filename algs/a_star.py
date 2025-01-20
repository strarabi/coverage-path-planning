from planner import Planner
from coverage_path import CoveragePath
import heapq

class AStar(Planner):
    def __init__(self):
        super().__init__()

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

    
    def plan(self, field):
        path=CoveragePath()
        pq=[] # priority queue
        heapq.heappush(pq, (0, field.start))
        cost_so_far={}
        cost_so_far[field.start] = 0
        path.add_node(field.start)

        while pq:
            _, node = heapq.heappop(pq)
            for neighbor in field.get_neighbors(node):
                new_cost = cost_so_far[node] + 1 # cost to travel to a neighbor is 1; could be changed based on field dynamics
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor]=new_cost
                    priority = new_cost + self._heuristic(node,neighbor)
                    heapq.heappush(pq, (priority, neighbor))
                    path.add_node(node)

        return path
