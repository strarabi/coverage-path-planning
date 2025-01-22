import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) # allow import from parent
from field import Field
from algs.a_star import AStar
from algs.wavefront_expansion import WavefrontExpansion
from algs.spanning_tree_coverage import SpanningTreeCoverage

simple_field = Field(
    10,
    10,
    [(1,1),(2,2),(3,3),(6,7), (9,9)],
    (0,0)
)

if __name__ == "__main__":
    planner = SpanningTreeCoverage(simple_field)
    path = planner.plan()
    simple_field.visualize_path(path)