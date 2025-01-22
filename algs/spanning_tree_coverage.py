from planner import Planner
from coverage_path import CoveragePath
import heapq
from collections import defaultdict


class SpanningTreeCoverage(Planner):
    def __init__(self, field):
        super().__init__(field)

    def prims(self):
        mst = defaultdict(list)
        visited = set()
        start = self.field.start
        edges = []

        visited.add(start)
        for neighbor in self.field.get_neighbors(start):
            weight = 1 # can use a custom cost function here if desired
            heapq.heappush(edges, (weight, start, neighbor))

        while edges:
            weight, node, neighbor = heapq.heappop(edges)
            if neighbor not in visited:
                mst[node].append(neighbor)
                mst[neighbor].append(node)
                visited.add(neighbor)

                for next_neighbor in self.field.get_neighbors(neighbor):
                    if next_neighbor not in visited:
                        weight = 1
                        heapq.heappush(edges, (weight, neighbor, next_neighbor))

        return mst

    def dfs(self, mst, node, visited, path):
        visited.add(node)
        path.append(node)

        for neighbor in mst[node]:
            if neighbor not in visited:
                self.dfs(mst, neighbor, visited, path)
                path.append(node)

    def plan(self):
        mst = self.prims()
        visited = set()
        path = []
        self.dfs(mst, self.field.start, visited, path)

        coverage_path = CoveragePath()
        for node in path:
            coverage_path.add_node(node)

        return coverage_path
