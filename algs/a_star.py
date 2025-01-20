from planner import Planner
from coverage_path import CoveragePath

class AStar(Planner):
    def __init__(self):
        super().__init__()

    def _heuristic(self, n1, n2):
        """
        Private function representing heuristic h(n) function for
        estimating cost to travel to neighbor. In this implementation,
        Manhattan distance is used, although several other options exist
        (see https://ics.uci.edu/~kkask/Fall-2016%20CS271/slides/03-InformedHeuristicSearch.pdf).
        """


    
    def plan(self, field):
        p=CoveragePath()
        pq=[] # priority queue



        return p
