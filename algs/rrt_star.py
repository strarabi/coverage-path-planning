from planner import Planner
from coverage_path import CoveragePath

class RRTStar(Planner):
    def __init__(self, field):
        super().__init__(field)
    
    def plan(self):
        return CoveragePath()