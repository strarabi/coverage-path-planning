from field import Field
from coverage_path import CoveragePath

class Planner:
    """
    Abstract class for a Coverage Path Planning algorithm.
    """
    def __init__(self):
        pass

    def plan(self, field: Field) -> CoveragePath:
        pass
