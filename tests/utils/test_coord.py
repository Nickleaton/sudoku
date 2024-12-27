import unittest

from src.utils.coord import Coord, CoordException


class TestCoord(unittest.TestCase):
    """Test cases for the Coord class."""

    def setUp(self):
        """Set up common Coord instances for testing."""
        self.coord_a = Coord(2, 3)
        self.coord_b = Coord(5, 7)
        self.coord_c = Coord(-3, -4)
        self.tolerance = 1e-9

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

    def test_division(self):
        """Test the division of Coord by a scalar."""
        result = self.coord_b / 2
        self.assertEqual(result, Coord(2.5, 3.5))

    def test_negation(self):
        """Test negation of a Coord object."""
        result = -self.coord_a
        self.assertEqual(result, Coord(-2, -3))

    def test_equality(self):
        """Test equality comparison with tolerance."""
        coord_d = Coord(2.000000001, 3.000000001)
        self.assertTrue(self.coord_a == coord_d)

        coord_e = Coord(2.1, 3.1)
        self.assertFalse(self.coord_a == coord_e)

    def test_parallel(self):
        # Test directions that are almost parallel but slightly off (within tolerance)
        direction_a = Coord(1.0, 1.0)  # Close to 45 angle_degree (diagonal)
        direction_b = Coord(1.0, 1.000000001)  # Slightly off, but still parallel
        self.assertTrue(direction_a.parallel(direction_b))

    def test_comparison(self):
        """Test less-than comparison of Coord objects."""
        self.assertTrue(self.coord_a < self.coord_b)
        self.assertFalse(self.coord_b < self.coord_a)

    def test_middle(self):
        """Test the calculation of the midpoint between two Coord objects."""
        result = Coord.middle(self.coord_a, self.coord_b)
        self.assertEqual(result, Coord(3.5, 5))

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
