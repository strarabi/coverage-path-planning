from planner import Planner
from collections import deque
from coverage_path import CoveragePath

class WavefrontExpansion(Planner):
    def __init__(self, field):
        super().__init__(field)
        self.node_labels = {}
        self.visited = set()
    
    def _bfs(self):
        node_label = 3 # start at 3, since 0, 1, and 2 are already used in the field
        q=deque()
        q.append(self.field.start)
        visited = set()

        while q:
            node = q.popleft()
            self.node_labels[node] = node_label
            node_label += 1
            visited.add(node)
            for neighbor in self.field.get_neighbors(node):
                if neighbor not in visited and neighbor not in q:
                    q.append(neighbor)

    def _min_reachable(self, node):
        cost = float('inf')
        result = None

        for neighbor in self.field.get_neighbors(node):
            if neighbor in self.node_labels and self.node_labels[neighbor] < cost and neighbor not in self.visited:
                cost = self.node_labels[neighbor]
                result = neighbor

        return result

    def plan(self):
        self._bfs()
        path = CoveragePath()
        end_node = max(self.node_labels, key=self.node_labels.get)
        path.add_node(end_node)
        self.visited.add(end_node)

        while not path.is_valid_path(self.field):
            node = path.peek_right()
            next_node = self._min_reachable(node)
            if next_node:
                path.add_node(next_node)
                self.visited.add(next_node)
            else:
                print("path is impossible")
                return None
        
        return path


