import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) # allow import from parent directory
from field import Field
from algs.a_star import AStar

simple_field = Field(
    10,
    10,
    [],
    (0,0)
)

if __name__ == "__main__":
    planner = AStar()
    path = planner.plan(simple_field)
    simple_field.visualize_path(0)