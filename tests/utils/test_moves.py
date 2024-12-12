import unittest

from src.utils.angle import Angle
from src.utils.coord import Coord
from src.utils.moves import Moves


class TestMoves(unittest.TestCase):

    def test_angle(self):
        """Test that the angle property is calculated correctly."""
        # Test the angle for RIGHT direction
        self.assertEqual(Moves.RIGHT.angle, Angle(0.0), 'RIGHT')
        self.assertEqual(Moves.UP.angle, Angle(90.0), 'UP')
        self.assertEqual(Moves.LEFT.angle, Angle(180.0), 'LEFT')
        self.assertEqual(Moves.DOWN.angle, Angle(270.0), 'DOWN')

        # Additional test for diagonal angles
        self.assertEqual(Moves.UP_LEFT.angle, Angle(135.0), 'UP_LEFT')
        self.assertEqual(Moves.UP_RIGHT.angle, Angle(45.0), 'UP_RIGHT')
        self.assertEqual(Moves.DOWN_LEFT.angle, Angle(225.0), 'DOWN_LEFT')
        self.assertEqual(Moves.DOWN_RIGHT.angle, Angle(315.0), 'DOWN_RIGHT')

    def test_parallel(self):
        """Test the parallel method for checking direction parallelism."""

        self.assertTrue(Moves.RIGHT.parallel(Moves.LEFT))
        self.assertTrue(Moves.RIGHT.parallel(Moves.RIGHT))
        self.assertTrue(Moves.UP.parallel(Moves.DOWN))
        self.assertTrue(Moves.UP.parallel(Moves.UP))
        self.assertTrue(Moves.UP_LEFT.parallel(Moves.DOWN_RIGHT))
        self.assertTrue(Moves.UP_LEFT.parallel(Moves.UP_LEFT))
        self.assertFalse(Moves.UP.parallel(Moves.LEFT))

    def test_directions(self):
        # Test directions that are almost parallel but slightly off (within tolerance)
        direction_a = Coord(1.0, 1.0)  # Close to 45 angle_degree (diagonal)
        direction_b = Coord(1.0, 1.000000001)  # Slightly off, but still parallel
        self.assertTrue(direction_a.parallel(direction_b))

    def test_orthogonals(self):
        expected = [
            Coord(0, -1),  # LEFT
            Coord(0, 1),  # RIGHT
            Coord(-1, 0),  # UP
            Coord(1, 0)  # DOWN
        ]
        self.assertEqual(Moves.orthogonals(), expected)

    def test_diagonals(self):
        expected = [
            Coord(-1, -1),  # UP_LEFT
            Coord(-1, 1),  # UP_RIGHT
            Coord(1, 1),  # DOWN_RIGHT
            Coord(1, -1)  # DOWN_LEFT
        ]
        self.assertEqual(Moves.diagonals(), expected)

    def test_kings(self):
        expected = [
            Coord(0, -1),  # LEFT
            Coord(0, 1),  # RIGHT
            Coord(-1, 0),  # UP
            Coord(1, 0),  # DOWN
            Coord(-1, -1),  # UP_LEFT
            Coord(-1, 1),  # UP_RIGHT
            Coord(1, 1),  # DOWN_RIGHT
            Coord(1, -1)  # DOWN_LEFT
        ]
        self.assertEqual(Moves.kings(), expected)

    def test_knights(self):
        expected = [
            Coord(-1, -2),
            Coord(1, -2),
            Coord(-2, -1),
            Coord(-2, 1),
            Coord(-1, 2),
            Coord(1, 2),
            Coord(2, 1),
            Coord(2, -1)
        ]
        self.assertEqual(Moves.knights(), expected)

    def test_all_directions(self):
        expected = [
            Coord(0, -1),  # LEFT
            Coord(0, 1),  # RIGHT
            Coord(-1, 0),  # UP
            Coord(1, 0),  # DOWN
            Coord(-1, -1),  # UP_LEFT
            Coord(-1, 1),  # UP_RIGHT
            Coord(1, 1),  # DOWN_RIGHT
            Coord(1, -1)  # DOWN_LEFT
        ]
        self.assertEqual(Moves.directions(), expected)

    def test_all(self):
        expected = [
            Coord(0, -1),  # LEFT
            Coord(0, 1),  # RIGHT
            Coord(-1, 0),  # UP
            Coord(1, 0),  # DOWN
            Coord(-1, -1),  # UP_LEFT
            Coord(-1, 1),  # UP_RIGHT
            Coord(1, 1),  # DOWN_RIGHT
            Coord(1, -1),  # DOWN_LEFT
            Coord(0, 0)  # CENTER
        ]
        self.assertEqual(Moves.all(), expected)


if __name__ == "__main__":
    unittest.main()
