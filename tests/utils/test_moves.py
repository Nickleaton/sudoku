"""TestMoves."""
import unittest

from src.utils.angle import Angle
from src.utils.coord import Coord
from src.utils.moves import Moves


class TestMoves(unittest.TestCase):
    """Test Moves class."""

    def test_angle(self):
        """Test the angle property calculation."""
        # Test the angle for right direction
        self.assertEqual(Moves.right.angle, Angle(0.0), 'right')
        self.assertEqual(Moves.up.angle, Angle(90.0), 'up')
        self.assertEqual(Moves.left.angle, Angle(180.0), 'left')
        self.assertEqual(Moves.down.angle, Angle(270.0), 'down')

        # Additional test for diagonal angles
        self.assertEqual(Moves.up_left.angle, Angle(135.0), 'up_left')
        self.assertEqual(Moves.up_right.angle, Angle(45.0), 'up_right')
        self.assertEqual(Moves.down_left.angle, Angle(225.0), 'down_left')
        self.assertEqual(Moves.down_right.angle, Angle(315.0), 'down_right')

    def test_parallel(self):
        """Test the parallel method for checking direction parallelism."""
        self.assertTrue(Moves.right.parallel(Moves.left))
        self.assertTrue(Moves.right.parallel(Moves.right))
        self.assertTrue(Moves.up.parallel(Moves.down))
        self.assertTrue(Moves.up.parallel(Moves.up))
        self.assertTrue(Moves.up_left.parallel(Moves.down_right))
        self.assertTrue(Moves.up_left.parallel(Moves.up_left))
        self.assertFalse(Moves.up.parallel(Moves.left))

    def test_directions(self):
        """Test directions that are almost parallel but slightly off (within tolerance)."""
        direction_a = Coord(1, 1)  # Close to 45 angle_degree (diagonal)
        direction_b = Coord(1000000000, 1000000001)  # Slightly off, but still parallel
        self.assertTrue(direction_a.parallel(direction_b))

    def test_orthogonals(self):
        """Test the orthogonals method for standard orthogonal directions."""
        expected = (
            Coord(0, -1),  # left
            Coord(0, 1),  # right
            Coord(-1, 0),  # up
            Coord(1, 0)  # down
        )
        self.assertEqual(Moves.orthogonals(), list(expected))

    def test_diagonals(self):
        """Test the diagonals method for standard diagonal directions."""
        expected = (
            Coord(-1, -1),  # up_left
            Coord(-1, 1),  # up_right
            Coord(1, 1),  # down_right
            Coord(1, -1)  # down_left
        )
        self.assertEqual(Moves.diagonals(), list(expected))

    def test_kings(self):
        """Test the kings method for king movement directions."""
        expected = (
            Coord(0, -1),  # left
            Coord(0, 1),  # right
            Coord(-1, 0),  # up
            Coord(1, 0),  # down
            Coord(-1, -1),  # up_left
            Coord(-1, 1),  # up_right
            Coord(1, 1),  # down_right
            Coord(1, -1)  # down_left
        )
        self.assertEqual(Moves.kings(), list(expected))

    def test_knights(self):
        """Test the knights method for knight movement directions."""
        expected = (
            Coord(-1, -2),
            Coord(1, -2),
            Coord(-2, -1),
            Coord(-2, 1),
            Coord(-1, 2),
            Coord(1, 2),
            Coord(2, 1),
            Coord(2, -1)
        )
        self.assertEqual(Moves.knights(), list(expected))

    def test_all_directions(self):
        """Test the all_directions method for all movement directions."""
        expected = (
            Coord(0, -1),  # left
            Coord(0, 1),  # right
            Coord(-1, 0),  # up
            Coord(1, 0),  # down
            Coord(-1, -1),  # up_left
            Coord(-1, 1),  # up_right
            Coord(1, 1),  # down_right
            Coord(1, -1)  # down_left
        )
        self.assertEqual(Moves.directions(), list(expected))

    def test_all_moves(self):
        """Test the all_moves method for all possible moves."""
        expected = (
            Coord(0, -1),  # left
            Coord(0, 1),  # right
            Coord(-1, 0),  # up
            Coord(1, 0),  # down
            Coord(-1, -1),  # up_left
            Coord(-1, 1),  # up_right
            Coord(1, 1),  # down_right
            Coord(1, -1),  # down_left
            Coord(0, 0)  # center
        )
        self.assertEqual(Moves.all_moves(), list(expected))

    def test_square(self):
        """Test the square method for generating a 2x2 square of coordinates."""
        expected = (
            Coord(0, 0),
            Coord(0, 1),
            Coord(1, 0),
            Coord(1, 1),
        )
        self.assertEqual(Moves.square(), list(expected))

    def test_monkeys(self):
        """Test the monkeys method for returning a specific set of coordinates."""
        expected = (
            Coord(-1, -3),
            Coord(1, -3),
            Coord(-3, -1),
            Coord(-3, 1),
            Coord(-1, 3),
            Coord(1, 3),
            Coord(3, 1),
            Coord(3, -1)
        )
        self.assertEqual(Moves.monkeys(), list(expected))

    def test_girandola(self):
        """Test the girandola method for returning the correct list of coordinates."""
        expected = (
            Coord(1, 1),
            Coord(1, 9),
            Coord(2, 5),
            Coord(5, 2),
            Coord(5, 5),
            Coord(5, 8),
            Coord(8, 5),
            Coord(9, 1),
            Coord(9, 9),
        )
        self.assertEqual(Moves.girandola(), list(expected))

    def test_asterix(self):
        """Test the asterix method for returning the correct list of coordinates."""
        expected = (
            Coord(2, 5),
            Coord(3, 3),
            Coord(3, 7),
            Coord(5, 2),
            Coord(5, 5),
            Coord(5, 8),
            Coord(7, 3),
            Coord(7, 7),
            Coord(8, 5),
        )
        self.assertEqual(Moves.asterix(), list(expected))

    def test_disjoint_9x9(self):
        """Test the disjoint_9x9 method for returning disjoint 3x3 grid coordinates."""
        expected = (
            Coord(0, 0), Coord(0, 3), Coord(0, 6),
            Coord(3, 0), Coord(3, 3), Coord(3, 6),
            Coord(6, 0), Coord(6, 3), Coord(6, 6),
        )
        result = Moves.disjoint9x9()
        self.assertEqual(result, list(expected))


if __name__ == "__main__":
    unittest.main()
