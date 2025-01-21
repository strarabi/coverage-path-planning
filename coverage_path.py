from field import Field

class CoveragePath:
    """
    Represents a coverage path through a field.
    """
    def __init__(self, path=[]):
        self.path=path
    
    def add_node(self, node: tuple):
        self.path.append(node)
    
    def is_valid_path(self, field: Field) -> bool:
        """
        Returns True if the CoveragePath is a valid coverage path through
        given Field and False otherwise.
        """
        length=field.length
        width=field.width
        for x in range(length):
            for y in range(width):
                if field.is_valid(x, y) and not ((x,y)) in self.path:
                    return False
        return True
    
    def peek_left(self) -> tuple:
        """
        Returns the leftmost node in the coverage path
        """
        return self.path[0]
    
    def peek_right(self) -> tuple:
        """
        Returns the rightmost node in the coverage path
        """
        return self.path[-1]
    
    def __str__(self):
        return str(self.path)