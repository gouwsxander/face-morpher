from dataclasses import dataclass

@dataclass
class Region:
    """A rectangular region of an image.

    Attributes:
        left_top: The coordinates of the top-left corner of the region.
        right_bottom: The coordinates of the bottom-right corner of the region.
        left: The x-coordinate of the left edge of the region.
        top: The y-coordinate of the top edge of the region.
        right: The x-coordinate of the right edge of the region. This must be greater than `left`.
        bottom: The y-coordinate of the bottom edge of the region. This must be greater than `top`.
    """
    left_top: tuple(int, int)
    right_bottom: tuple(int, int)
    
    def __post_init__(self):
        """Sets left, top, right, and bottom values and checks they are consistent.
        
        Raises:
            ValueError: Bounds inconsistent with eachother.
        """
        self.left: int = self.left_top[0]
        self.top: int = self.left_top[1]
        self.right: int = self.right_bottom[0]
        self.bottom: int = self.right_bottom[1]

        if not self.left < self.right or not self.top < self.bottom:
            raise ValueError("Left bound must be smaller than right and top bound must be smaller than bottom bound.")

    def contains(self, other: 'Region' | tuple(int, int)) -> bool:
        """Returns true iff other argument is completely contained by self.
        
        Args:
            other: Region or tuple(int, int) that is being checked.
        """
        if isinstance(other, Region):
            is_horizontally_contained = self.left < other.left and self.right > other.right
            is_vertically_contained = self.top < other.top and self.bottom > other.bottom
            return is_vertically_contained and is_horizontally_contained
        
        elif isinstance(other, tuple(int, int)):
            is_horizontally_contained = self.left < other[0] < self.right
            is_vertically_contained = self.top < other[1] < self.bottom
            return is_vertically_contained and is_horizontally_contained
        
        else:
            raise TypeError("`other` argument must be point or region.")

    def intersects(self, other: 'Region') -> bool:
        """Returns true iff other region has some overlap with self.
        
        Args:
            other: Region that is being checked for intersection.
        """
        is_other_in_self = self.contains(other.left_top) or self.contains(other.right_bottom)
        is_self_in_other = other.contains(self.left_top) or other.contains(self.right_bottom)

        return is_other_in_self or is_self_in_other


@dataclass
class Warp:
    source: Region
    target: Region
    bounding: Region

    def _check_validity(self):
        return 
    
    def __post_init__(self):
        if not self.bounding.contains(self.source) or not self.bounding.contains(self.target):
            raise ValueError("Bounding region must contain source and target regions.")