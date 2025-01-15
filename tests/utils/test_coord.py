import unittest

from src.utils.coord import Coord, CoordException


class TestCoord(unittest.TestCase):
    """Test cases for the Coord class."""

    def setUp(self):
        """Set up common Coord instances for testing."""
        self.coord_a = Coord(2, 3)
        self.coord_b = Coord(5, 7)
        self.coord_c = Coord(-3, -4)


Te
    def test_addition(self):
        """Test the addition of two Coord objects."""
        result = self.coord_a + self.coord_b
        self.assertEqual(result, Coord(7, 10))

    def test_subtraction(self):
        """Test the subtraction of two Coord objects."""
        result = self.coord_b - self.coord_a
        self.assertEqual(result, Coord(3, 4))

    def test_multiplication(self):
        """Test the multiplication of Coord by a scalar and another Coord."""
        scalar_result = self.coord_a * 2
        self.assertEqual(scalar_result, Coord(4, 6))

        coord_result = self.coord_a * self.coord_b
        self.assertEqual(coord_result, Coord(10, 21))

        with self.assertRaises(CoordException):
            _ = self.coord_a * "invalid"

    def test_negation(self):
        """Test negation of a Coord object."""
        result = -self.coord_a
        self.assertEqual(result, Coord(-2, -3))

    def test_parallel(self):
        # Test directions that are almost parallel
        direction_a = Coord(1, 1)
        direction_b = Coord(1, 1)
        direction_c = Coord(1, 9)
        self.assertTrue(direction_a.parallel(direction_b))
        self.assertFalse(direction_a.parallel(direction_c))

    def test_comparison(self):
        """Test less-than comparison of Coord objects."""
        self.assertTrue(self.coord_a < self.coord_b)
        self.assertFalse(self.coord_b < self.coord_a)


    def test_create_from_int(self):
        """Test creation of Coord from an integer representation."""
        result = Coord.create_from_int(23)
        self.assertEqual(result, Coord(2, 3))

    def test_validate(self):
        """Test validation of YAML-style input."""
        valid_input = [2, 3]
        invalid_input = ["row", "column"]

        self.assertEqual(Coord.validate(valid_input), [])
        self.assertIn("row not integer", Coord.validate(invalid_input))


if __name__ == "__main__":
    unittest.main()
