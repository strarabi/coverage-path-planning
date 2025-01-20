from field import Field

class CoveragePath:
    """
    Represents a coverage path through a field.
    """
    def __init__(self, path=set()):
        self.path=path
    
    def add_node(self, x,y):
        self.path.add((x,y))
    
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