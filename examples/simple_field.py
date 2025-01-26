import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) # allow import from parent
from field import Field
from algs.a_star import AStar
from algs.wavefront_expansion import WavefrontExpansion
from algs.spanning_tree_coverage import SpanningTreeCoverage
from algs.bcd import BoustrophedonCellularDecomposition
from algs.ba_star import BAStar

simple_field = Field(
    10,
    10,
    [(1, 0), (1, 1), (1, 2), (1, 3), (4, 4), (4, 5), (4, 6), (7, 7), (7, 8), (7, 9)],
    (0,0)
)

if __name__ == "__main__":
    planner = BAStar(simple_field)
    path = planner.plan()
    print(path)
    simple_field.visualize_path(path)