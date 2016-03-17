import random
from unittest import TestCase
from ps2 import Position, RectangularRoom, Robot
from test_rectangularRoom import TestRectangularRoom

__author__ = 'Sam Broderick'


WIDTH = 100
HEIGHT = 100


class TestRobot(TestCase):
    def setUp(self):
        global room, speed
        global w, h
        w = random.randint(0, WIDTH)
        h = random.randint(0, HEIGHT)
        room = RectangularRoom(w, h)
        speed = random.random() * room.width/10.0
        self.test_robot = Robot(room, speed)

    def test_getRobotPosition(self):
        pos = self.test_robot.getRobotPosition()
        self.assertTrue(isinstance(pos, Position),
                        'getRobotPosition failed to return obj')
        self.assertTrue(0 <= pos.getX() < room.width,
                        'getRandomPosition returned out of bound x')
        self.assertTrue(0 <= pos.getY() < room.height,
                        'getRandomPosition returned out of bound y')

    def test_getRobotDirection(self):
        self.fail()

    def test_setRobotPosition(self):
        self.fail()

    def test_setRobotDirection(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))