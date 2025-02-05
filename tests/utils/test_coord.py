import unittest

from src.utils.coord import Coord, CoordError


class TestCoord(unittest.TestCase):
    """Test cases for the Coord class."""

    def test_coord_hash(self):
        # Create two Coord instances with the same values
        coord1 = Coord(1, 2)
        coord2 = Coord(1, 2)

        # Create two Coord instances with different values
        coord3 = Coord(2, 3)

        # Assert that the hash values for equal coordinates are the same
        self.assertEqual(hash(coord1), hash(coord2), "Hashes should be equal for the same coordinates")

        # Assert that the hash values for different coordinates are not the same
        self.assertNotEqual(hash(coord1), hash(coord3), "Hashes should be different for different coordinates")

    if __name__ == '__main__':
        unittest.main()

    def test_addition(self):
        """Test the addition of two Coord objects."""
        coord_a = Coord(2, 3)
        coord_b = Coord(5, 7)
        result = coord_a + coord_b
        self.assertEqual(result, Coord(7, 10))

    def test_subtraction(self):
        """Test the subtraction of two Coord objects."""
        coord_a = Coord(2, 3)
        coord_b = Coord(5, 7)
        result = coord_b - coord_a
        self.assertEqual(result, Coord(3, 4))

    def test_multiplication(self):
        """Test the multiplication of Coord by a scalar and another Coord."""
        coord_a = Coord(2, 3)
        coord_b = Coord(5, 7)

        # Scalar multiplication
        scalar_result = coord_a * 2
        self.assertEqual(scalar_result, Coord(4, 6))

        # Coord multiplication
        coord_result = coord_a * coord_b
        self.assertEqual(coord_result, Coord(10, 21))

        with self.assertRaises(CoordError):
            _ = coord_a * "invalid"

    def test_create_from_int(self):
        """Test creation of Coord from an integer representation."""
        result = Coord.create_from_int(23)
        self.assertEqual(result, Coord(2, 3))

    # def test_validate(self):
    #     """Test validation of YAML-style input."""
    #     valid_input = [2, 3]
    #     invalid_input = ["row", "column"]
    #
    #     self.assertEqual(Coord.validate(valid_input), [])
    #     self.assertIn("row not integer", Coord.validate(invalid_input))

    def test_top_left(self):
        """Test the top_left property."""
        coord: Coord = Coord(2, 2)
        self.assertEqual(Coord(2, 2), coord.top_left)

    def test_top_right(self):
        """Test the top_right property."""
        coord: Coord = Coord(2, 2)
        self.assertEqual(Coord(2, 3), coord.top_right)

    def test_bottom_left(self):
        """Test the bottom_left property."""
        coord: Coord = Coord(2, 2)
        self.assertEqual(Coord(3, 2), coord.bottom_left)

    def test_bottom_right(self):
        """Test the bottom_right property."""
        coord: Coord = Coord(2, 2)
        self.assertEqual(Coord(3, 3), coord.bottom_right)

    def test_neg(self):
        """Test the __neg__ method (negating a Coord)."""
        self.assertEqual(-Coord(2, 3), Coord(-2, -3))

    def test_eq(self):
        """Test the __eq__ method (equality comparison)."""
        self.assertTrue(Coord(2, 3) == Coord(2, 3))
        self.assertFalse(Coord(2, 4) == Coord(2, 3))
        self.assertFalse(Coord(3, 3) == Coord(2, 3))
        self.assertFalse(Coord(4, 4) == Coord(2, 3))
        with self.assertRaises(CoordError):
            _ = Coord(2, 3) == "string"  # Invalid comparison

    def test_lt(self):
        """Test the __lt__ method (less than comparison)."""
        self.assertTrue(Coord(2, 3) < Coord(2, 4))
        self.assertTrue(Coord(1, 3) < Coord(2, 3))
        self.assertTrue(Coord(1, 1) < Coord(2, 3))

        self.assertFalse(Coord(2, 3) < Coord(2, 3))
        self.assertFalse(Coord(3, 3) < Coord(2, 3))
        self.assertFalse(Coord(2, 4) < Coord(2, 3))
        self.assertFalse(Coord(4, 4) < Coord(2, 3))
        with self.assertRaises(CoordError):
            _ = Coord(2, 4) < "string"  # Invalid comparison

    def test_parallel(self):
        """Test the parallel method (checking if two coordinates are parallel)."""
        # Assuming angle is implemented and comparison works
        self.assertTrue(Coord(2, 2).parallel(Coord(1, 1)))  # example if parallel
        self.assertTrue(Coord(1, 1).parallel(Coord(2, 2)))  # example if not parallel
        self.assertFalse(Coord(2, 2).parallel(Coord(3, 4)))  # example if not parallel

    def test_is_orthogonal(self):
        """Test the is_orthogonal method (checking orthogonal alignment)."""
        self.assertTrue(Coord(2, 3).is_orthogonal(Coord(3, 3)))  # Same column, vertical alignment
        self.assertTrue(Coord(2, 3).is_orthogonal(Coord(2, 4)))  # Same row, horizontal alignment
        self.assertFalse(Coord(2, 3).is_orthogonal(Coord(1, 5)))  # Neither vertical nor horizontal

    def test_is_vertical(self):
        """Test the is_vertical method (checking vertical alignment)."""
        self.assertTrue(Coord(2, 3).is_vertical(Coord(3, 3)))  # Same column
        self.assertFalse(Coord(2, 3).is_vertical(Coord(2, 4)))  # Different column

    def test_is_horizontal(self):
        """Test the is_horizontal method (checking horizontal alignment)."""
        self.assertTrue(Coord(2, 3).is_horizontal(Coord(2, 4)))  # Same row
        self.assertFalse(Coord(2, 3).is_horizontal(Coord(3, 3)))  # Different row


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()
