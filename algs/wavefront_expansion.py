from planner import Planner
from collections import deque
from coverage_path import CoveragePath

class WavefrontExpansion(Planner):
    def __init__(self, field):
        super().__init__(field)
        self.node_labels = {}
        self.visited = set()
    
    def _bfs(self):
        node_label = 2 # start at 3, since 0, and 1 are already used in the field
        q=deque()
        q.append(self.field.start)
        visited = set()
        visited.add(self.field.start)

        while q:
            qLen=len(q)
            for _ in range(qLen):
                node = q.popleft()
                self.node_labels[node] = node_label
                for neighbor in self.field.get_neighbors(node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            node_label += 1

    def plan(self):
        self._bfs()
        plan = CoveragePath()
        print(self.node_labels)
        sorted_nodes = sorted(self.node_labels.items(), key=lambda x: x[1])
        for node, _ in sorted_nodes:
            plan.add_node(node)
        return plan
