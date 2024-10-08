from math import sin, pi, cos

class Polygon:
    """
    A class to represent a regular strictly convex polygon.

    Attributes
    ----------
    edges : int
        The number of edges (and vertices) of the polygon.
    circumradius : float
        The circumradius of the polygon (distance from the center to a vertex).
    """

    def __init__(self, edges: int, circumradius: float) -> None:
        """
        Initializes a Polygon with a given number of edges and circumradius.

        edges : int
            The number of edges (and vertices) of the polygon. Must be >= 3.
        circumradius : float
            The circumradius of the polygon (distance from the center to a vertex).
        """
        if edges < 3:
            raise ValueError("A polygon must have at least 3 edges.")
        self._edges = edges
        self._circumradius = circumradius
    
    @property
    def count_vertices(self) -> int:
        """
        Returns the number of vertices (equal to the number of edges) of the polygon.
        """
        return self._edges

    @property
    def count_edges(self) -> int:
        """
        Returns the number of edges of the polygon.
        """
        return self._edges

    @property
    def circumradius(self) -> float:
        """
        Returns the circumradius of the polygon.
        """
        return self._circumradius

    @property
    def interior_angle(self) -> float:
        """
        Returns the interior angle of the polygon.
        """
        return (self._edges - 2) * (180 / self._edges)

    @property
    def edge_length(self) -> float:
        """
        Returns the length of each edge of the polygon.
        """
        return 2 * self._circumradius * sin(pi / self._edges)

    @property
    def apothem(self) -> float:
        """
        Returns the apothem of the polygon (distance from the center to the midpoint of an edge).
        """
        return self._circumradius * cos(pi / self._edges)

    @property
    def area(self) -> float:
        """
        Returns the area of the polygon.
        """
        return 0.5 * self._edges * self.edge_length * self.apothem

    @property
    def perimeter(self) -> float:
        """
        Returns the perimeter of the polygon.
        """
        return self._edges * self.edge_length

    def __repr__(self) -> str:
        """
        Returns a string representation of the Polygon instance.
        """
        return f"Polygon(n={self._edges}, R={self._circumradius})"
        
    def __eq__(self, other: object) -> bool:
        """
        Checks if two Polygon instances are equal.
        """
        if isinstance(other, Polygon):
            return (self._edges == other._edges 
                    and self._circumradius == other._circumradius)
        return NotImplemented
        
    def __gt__(self, other: object) -> bool:
        """
        Compares two Polygon instances based on the number of vertices.
        """
        if isinstance(other, Polygon):
            return self.count_vertices > other.count_vertices
        return NotImplemented
