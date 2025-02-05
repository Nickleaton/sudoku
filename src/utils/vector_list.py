"""VectorList."""
from src.utils.coord_list import CoordList


class VectorListError(Exception):
    """Exception raised for errors in VectorList operations."""
    pass


class VectorList:
    """Represents a collection of Vectors with various utility methods."""

    def __init__(self, vectors=None):
        """Initialize the VectorList with a given list of Vectors or an empty list."""
        self.vectors = [] if vectors is None else list(vectors)

    def __iter__(self):
        """Return an iterator over the vectors."""
        return iter(self.vectors)

    def __getitem__(self, index):
        """Retrieve the vector at the specified index."""
        return self.vectors[index]

    def __contains__(self, vector):
        """Check if a vector is in the VectorList."""
        return vector in self.vectors

    def __len__(self):
        """Return the number of vectors."""
        return len(self.vectors)

    def __repr__(self):
        """Return a string representation of the VectorList."""
        return f'{self.__class__.__name__}([{", ".join(map(repr, self.vectors))}])'

    def __eq__(self, other):
        """Check equality with another VectorList."""
        if not isinstance(other, VectorList):
            raise VectorListError(f'Cannot compare {type(other).__name__} with {self.__class__.__name__}')
        return self.vectors == other.vectors

    def extend(self, other):
        """Extend the VectorList with another VectorList."""
        if not isinstance(other, VectorList):
            raise VectorListError(f'Cannot extend with {type(other).__name__}')
        self.vectors.extend(other.vectors)

    def __add__(self, other):
        """Return a new VectorList combining both lists."""
        if not isinstance(other, VectorList):
            raise VectorListError(f'Cannot add {type(other).__name__}')
        return VectorList(self.vectors + other.vectors)

    def sort(self):
        """Sort the vectors in place."""
        self.vectors.sort()

    def merge_vectors(self):
        """Merge parallel vectors that share endpoints."""
        merged_vectors = []
        for vector in self.vectors:
            for index, merged_vector in enumerate(merged_vectors):
                if vector.mergeable(merged_vector):
                    merged_vectors[index] = vector.merge(merged_vector)
                    break
            else:
                merged_vectors.append(vector)
        return VectorList(sorted(merged_vectors))

    def find(self, coord):
        """Find the endpoint of a vector that starts or ends at a given coordinate."""
        endpoint_map = {v.start: v.end for v in self.vectors}
        endpoint_map.update({v.end: v.start for v in self.vectors})
        return endpoint_map.get(coord)

    @property
    def coords(self):
        """Return a CoordList of all unique coordinates in the VectorList."""
        coords = CoordList([])
        for vector in self.vectors:
            coords.add(vector.start)
            coords.add(vector.end)
        return coords
