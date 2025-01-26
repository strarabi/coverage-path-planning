from planner import Planner
from coverage_path import CoveragePath

class BoustrophedonCellularDecomposition(Planner):
    def __init__(self, field):
        super().__init__(field)
        self.model = []
        self.backtrack = []
    
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


    def plan(self):
        path = CoveragePath()
        self._boustrophedon_motion(self.field.start)
        for n in self.model:
            path.add_node(n)
        return path
