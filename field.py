from typing import List
import matplotlib
import matplotlib.pyplot as plt

class Field:
    """
    A configuration space representing a field being navigated by an unmanned aerial vehicle.
    In this implementation, a field is implemented as a matrix with 0 representing free space,
    1 representing an obstacle, and 2 representing the starting point. 
    """
    def __init__(self, length: int, width: int, obstacles: List[tuple], start: tuple):
        self.length = length
        self.width = width
        self.obstacles=set(obstacles)
        self.start = start
        self.vals = {} # maps (x,y) tuples to one of [0, 1, 2]
        self._initialize_vals()
    
    def _initialize_vals(self):
        """
        Private method which initializes self.vals with mappings:
        each node is mapped to either 0, 1, or 2 based on the parameters
        passed to __init__().
        """
        for x in range(self.length):
            for y in range(self.width):
                pt = (x,y)
                if pt == self.start:
                    self.vals[pt] = 2
                elif pt in self.obstacles:
                    self.vals[pt] = 1
                else:
                    self.vals[pt] = 0
    
    def is_valid(self, x, y) -> bool:
        """
        Returns True if (x,y) is free of obstacles and within the configuration space,
        and False otherwise.
        """
        if not (0<=x<=self.length and 0<=y<=self.width):
            return False
        return (x,y) not in self.obstacles

    def get_neighbors(self, node: tuple, diag=True):
        """
        Gets the neighbors for a node. If diag is True,
        uses Moore neighborhood (includes diagonal neighbors),
        otherwise uses Von Neumann neighborhood.
        """
        neighbors=[]
        x,y=node
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        if diag:
            directions += [(1,1), (-1,-1), (1,-1), (-1,1)]
        for dx,dy in directions:
            nx,ny=dx+x,dy+y
            if self.is_valid(nx,ny):
                neighbors.append((nx,ny))
        return neighbors

    def visualize_path(self, path):
        """
        Visualizes the field and path using matplotlib. Note the visualization
        requires the entire field to be loaded in memory, so this is not recommended
        for experiments with large fields.
        """
        M=[[0] * self.length] * self.width
        
        plt.imshow(M,cmap='Set2')
        print(path.path)
        X = [p[0] for p in path.path]
        Y = [p[1] for p in path.path]
        for i in range(0, len(X), 2):
            plt.plot(X[i:i+2], Y[i:i+2], 'ro-')
        for obs in self.obstacles:
            x,y=obs
            plt.plot(x, y, 'ko')
        plt.show()
