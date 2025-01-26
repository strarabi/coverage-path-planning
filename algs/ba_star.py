from planner import Planner
from coverage_path import CoveragePath
import heapq

class BAStar(Planner):
    """
    BA* algorithm based on https://link.springer.com/article/10.1007/s10489-012-0406-4.
    """
    def __init__(self, field):
        super().__init__(field)
        self.model = []
        self.visited = set()
        self.backtrack_points = []

    def _heuristic(self, n1: tuple, n2: tuple):
        """Manhattan distance heuristic for A*."""
        x1, y1 = n1
        x2, y2 = n2
        return abs(x1 - x2) + abs(y1 - y2)

    def _is_critical_point(self, node):
        """Returns True if current node has no unvisited neighbors and False otherwise"""
        neighbors = self.field.get_neighbors(node)
        return all(n in self.visited for n in neighbors)

    def _choose_next_cell(self, neighbors, direction):
        """Returns next cell based on boustrophedon direction."""
        sorted_neighbors = sorted(neighbors, key=lambda x: x[1])
        return sorted_neighbors[0] if direction == 1 else sorted_neighbors[-1]

    def _boustrophedon_motion(self, start):
        """Perform boustrophedon coverage from start until a critical point is reached."""
        curr = start
        direction = 1  # 1 for right, -1 for left

        while True:
            self.model.append(curr)
            self.visited.add(curr)
            neighbors = self.field.get_neighbors(curr)
            unvisited_neighbors = [n for n in neighbors if n not in self.visited]

            if not unvisited_neighbors: # we are at a critical point
                break

            same_row = [n for n in unvisited_neighbors if n[0] == curr[0]]
            if same_row:
                next_cell = self._choose_next_cell(same_row, direction)
            else:
                direction *= -1
                next_cell = unvisited_neighbors[0]

            curr = next_cell

    def _aStar(self, start, goal):
        """Returns a path from start to goal using A*."""
        open_heap = []
        heapq.heappush(open_heap, (0, start))
        came_from = {}
        g_score = {start: 0}

        while open_heap:
            current = heapq.heappop(open_heap)[1]

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor in self.field.get_neighbors(current):
                tentative_g = g_score[current] + 1  # can use a custom cost function here if desired
                if neighbor not in g_score or tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self._heuristic(neighbor, goal)
                    heapq.heappush(open_heap, (f, neighbor))

        return []  # path is impossible

    def _find_backtrack_points(self):
        """Returns a list of potential backtracking points."""
        backtrack_points = []
        for cell in self.model:
            for neighbor in self.field.get_neighbors(cell):
                if neighbor not in self.visited:
                    backtrack_points.append(cell)
                    break
        return backtrack_points

    def plan(self):
        path = CoveragePath()
        self.model = []
        self.visited = set()
        current = self.field.start

        while True:
            self._boustrophedon_motion(current)
            if path.is_valid_path(self.field):
                break

            backtrack_points = self._find_backtrack_points()
            if not backtrack_points:
                break  # if there are no backtrack points, we are done

            current_pos = self.model[-1]
            nearest = min(backtrack_points, key=lambda p: self._heuristic(current_pos, p))

            astar_path = self._aStar(current_pos, nearest)
            if not astar_path:
                break # if we cannot create a backtracking path, the field is impossible to cover

            for cell in astar_path[1:]:
                self.model.append(cell)
                self.visited.add(cell)

            current = nearest

        for cell in self.model:
            path.add_node(cell)
        return path