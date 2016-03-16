from unittest import TestCase
from ps2 import RectangularRoom
from ps2 import Position
import random


__author__ = 'Sam Broderick'

WIDTH = 100
HEIGHT = 100


class TestRectangularRoom(TestCase):
    def setUp(self):
        global w, h
        w = random.randint(0, WIDTH)
        h = random.randint(0, HEIGHT)
        self.room = RectangularRoom(w, h)

    def test_cleanTileAtPosition(self):
        global w, h

        m = random.randint(0, w)
        n = random.randint(0, h)

        pos = Position(m, n)
        self.room.cleanTileAtPosition(pos)
        self.assertEqual(self.room.isTileCleaned(m, n), True,
                         'cleanTile failed (or isTiledCleaned broken)')

    def test_isTileCleaned(self):
        m = random.randint(0, WIDTH)
        n = random.randint(0, HEIGHT)

        pos = Position(m, n)
        self.room.cleanTileAtPosition(pos)
        self.assertTrue(self.room.isTileCleaned(m, n),
                        'isTileCleaned failed or clean tile')

    def test_getNumTiles(self):
        global w, h
        num_tiles = w * h
        self.assertEqual(self.room.getNumTiles(), num_tiles,
                         'getNumTiles did not return w * h')

    def test_getNumCleanedTiles(self):
        self.assertTrue(self.room.getNumCleanedTiles() == 1,
                        'getNumCleanedTiles failed')

    def test_getRandomPosition(self):
        pos = self.room.getRandomPosition()
        self.assertTrue(isinstance(pos, Position),
                        'getRandomPosition failed to return obj')
        self.assertTrue(0 <= pos.getX() < WIDTH,
                        'getRandomPosition returned out of bound x')
        self.assertTrue(0 <= pos.getY() < HEIGHT,
                        'getRandomPosition returned out of bound y')

    def test_isPositionInRoom(self):
        global w, h

        pos = self.room.getRandomPosition()
        self.assertTrue(self.room.isPositionInRoom(pos),
                        'isPositionInRoom OK for random position in room')

        outside_pos = Position(w + 1, h + 1)
        self.assertFalse(self.room.isPositionInRoom(outside_pos),
                         'isPositionInRoom OK for position outside of room')

        negative_pos = Position(-0.5, -0.5)
        self.assertFalse(self.room.isPositionInRoom(negative_pos),
                         'isPositionInRoom OK for negative position')


if __name__ == '__main__':
    unittest.main()
