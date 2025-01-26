from planner import Planner
from coverage_path import CoveragePath
import heapq

class BAStar(Planner):
    """
    BA* algorithm defined in https://link.springer.com/article/10.1007/s10489-012-0406-4
    """
    def __init__(self, field):
        super().__init__(field)
        self.model = []
        self.backtrack = []

    def _heuristic(self, n1: tuple, n2: tuple):
        """
        Returns Manhattan distance between n1 and n2.
        """
        x1,y1=n1
        x2,y2=n2
        return abs(x1-x2) + abs(y1-y2)
    
    def _is_critical_point(self, node) -> bool:
        """Returns True if given (x,y) pair is a critical point"""
        return self.field.get_neighbors(node) == []
    
    def _choose_next_cell(self, neighbors, direction):
        return neighbors[0] if direction == 1 else neighbors[-1]
    
    def _boustrophedon_motion(self, start):
        curr = start
        self.model.append(curr)
        visited = set([curr])
        direction = 1

        while True:
            neighbors = self.field.get_neighbors(curr)
            unvisited_neighbors = [neighbor for neighbor in neighbors if neighbor not in visited]

            if not unvisited_neighbors:
                print("Critical point reached: No neighbors available. Finishing boustrophedon motion.")
                break
            
            if unvisited_neighbors:
                curr = self._choose_next_cell(unvisited_neighbors, direction)
                visited.add(curr)
                self.model.append(curr)
            else:
                direction *= -1
                neighbors = self.field.get_neighbors(curr)


    def _aStar(self, n1: tuple, n2: tuple) -> list:
        """
        Returns shortest path from n1 to n2 using A*.
        """
        pq = [] # priority queue
        heapq.heappush(pq, (0, n1))
        path = []
        path.append(n1)
        while pq:
            _, node = heapq.heappop(pq)
            path.append(node)
            if node == n2:
                return path
            for neighbor in self.field.get_neighbors(node):
                heapq.heappush(pq, (1 + self._heuristic(neighbor, n2)))
        return "path does not exist"

    def plan(self):
        path = CoveragePath()
        self._boustrophedon_motion(self.field.start)
        for n in self.model:
            path.add_node(n)
        return path
