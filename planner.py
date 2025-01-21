from field import Field
from coverage_path import CoveragePath

class Planner:
    """
    Abstract class for a Coverage Path Planning algorithm.
    """
    def __init__(self, field: Field):
        self.field = field

    def plan(self) -> CoveragePath:
        pass
