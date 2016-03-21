# 6.00.2x Problem Set 2: Simulating robots

# import abc
import math
import matplotlib
import random
import pylab
import Tkinter


from ps2_visualize import *

# For Python 2.7:
# from ps2_verify_movement27 import testRobotMovement


# If you get a "Bad magic number" ImportError, you are not using
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """

    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    # TODO P1.1: DONE Initializing the object
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height

        # implement cleaned? as a dict and initialize to False for all tiles
        self.cleaned = dict()
        for i in range(width):
            for j in range(height):
                self.cleaned[(i, j)] = False

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        :param pos: Position object
        """
        # TODO P1.2: DONE Marking an appropriate tile as cleaned when a robot
        """
        moves to a given position (casting floats to ints - and/or the
        function math.floor - may be useful to you here)
        """
        x = int(pos.getX())
        y = int(pos.getY())
        self.cleaned[(x, y)] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        :rtype: bool
        :param m: tile x-coordinate
        :param n: tile y-coordinate
        """
        # TODO P1.3: DONE Determining if a given tile has been cleaned
        return self.cleaned[(m, n)]

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO P1.4: DONE Determining how many tiles there are in the room
        return len(self.cleaned)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO P1.5: DONE Determining how many cleaned tiles there are in the room
        number_cleaned = 0  # initialize
        for v in self.cleaned.itervalues():  # iterate over values
            if v:
                number_cleaned += 1
        return number_cleaned

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        :rtype: object
        """
        # TODO P1.6: DONE Getting a random position in the room
        m = random.randrange(0, self.width)
        n = random.randrange(0, self.height)
        return Position(m, n)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        # TODO P1.7: Determining if a given position is in the room

        x = math.floor(pos.getX())
        y = math.floor(pos.getY())

        # implemented as checking if key in dictionary of cleaned status
        return (x, y) in self.cleaned


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    # __metaclass__ = abc.ABCMeta

    # TODO P1.8: DONE Initializing the object

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        :type speed: float
        """
        self.room = room
        self.speed = speed
        self.robot_position = self.room.getRandomPosition()
        self.direction = random.randint(0, 359)  # 359 since randint is a closed interval
        self.room.cleanTileAtPosition(self.robot_position)

    # TODO 1.9 DONE Accessing the robot's position

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        assert isinstance(self.robot_position, Position)
        return self.robot_position

    # TODO 1.10 DONE Accessing the robot's direction

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        assert 0 <= self.direction < 360
        return self.direction

    # TODO 1.11: DONE Setting the robot's position

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        :param position: a Position object.
        """
        assert isinstance(position, Position)
        self.robot_position = position

    # TODO 1.12 DONE Setting the robot's direction

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        :param direction: integer representing an angle in degrees
        :type direction: int
        """
        assert 0 <= direction < 360
        self.direction = direction

    # @abc.abstractmethod
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError  # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        new_pos = self.robot_position.getNewPosition(self.direction, self.speed)
        new_direction = self.getRobotDirection()
        while not self.room.isPositionInRoom(new_pos):
            new_direction = random.randint(0, 359)
            new_pos = self.robot_position.getNewPosition(new_direction, self.speed)
        self.setRobotPosition(new_pos)
        self.setRobotDirection(new_direction)
        self.room.cleanTileAtPosition(self.getRobotPosition())


# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    :type robot_type: object
    :type min_coverage: float
    :param num_trials: an int (num_trials > 0)
    :type num_robots: int
    :param num_robots: an int (num_robots > 0)
    :param robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    trial_rooms = []
    time_steps = []

    for n in range(num_trials):
        trial_rooms.append(RectangularRoom(width, height))
        trial_room = trial_rooms[n]
        robots = []  # list for robot objects
        robot_positions = []

        # spawn robot objects and add them to the robots list
        for i in range(0, num_robots):
            robots.append(robot_type(trial_room, speed))
            r = robots[i]

            # avoid 2 robots in the same position
            while r.getRobotPosition() in robot_positions:
                # generate new robot positions until not in occupied position
                robots[i].setRobotPosition(trial_room.getRandomPosition())
            robot_positions.append(r.getRobotPosition())

        coverage = trial_room.getNumCleanedTiles() / float(
            trial_room.getNumTiles())
        time_step = 0

        while coverage < min_coverage:
            for r in robots:
                r.updatePositionAndClean()
            num_cleaned = trial_room.getNumCleanedTiles()
            num_tiles = trial_room.getNumTiles()
            coverage = num_cleaned / float(num_tiles)
            time_step += 1
        time_steps.append(time_step)

    return sum(time_steps) / float(len(time_steps))


# Uncomment this line to see how much your simulation takes on average
print('===== StandardRobot =====')
print('1 robot, 5 x 5, 100% coverage')
print(runSimulation(1, 1.0, 5, 5, 1.0, 30, StandardRobot))
print('1 robot, 10 x 10, 75% coverage')
print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))
print('1 robot, 10 x 10, 90% coverage')
print(runSimulation(1, 1.0, 10, 10, 0.9, 30, StandardRobot))
print('1 robot, 20 x 20, 100% coverage')
print(runSimulation(1, 1.0, 20, 20, 1.0, 30, StandardRobot))
print('3 robot, 20 x 20, 100% coverage')
print(runSimulation(3, 1.0, 20, 20, 1.0, 30, StandardRobot))


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        new_direction = random.randint(0, 359)
        new_pos = self.robot_position.getNewPosition(new_direction, self.speed)
        while not self.room.isPositionInRoom(new_pos):
            new_direction = random.randint(0, 359)
            new_pos = self.robot_position.getNewPosition(new_direction, self.speed)
        self.setRobotPosition(new_pos)
        self.setRobotDirection(new_direction)
        self.room.cleanTileAtPosition(self.getRobotPosition())


print('===== RandomWalkRobot =====')
print('1 robot, 5 x 5, 100% coverage')
print(runSimulation(1, 1.0, 5, 5, 1.0, 30, RandomWalkRobot))
print('1 robot, 10 x 10, 75% coverage')
print(runSimulation(1, 1.0, 10, 10, 0.75, 30, RandomWalkRobot))
print('1 robot, 10 x 10, 90% coverage')
print(runSimulation(1, 1.0, 10, 10, 0.9, 30, RandomWalkRobot))
print('1 robot, 20 x 20, 100% coverage')
print(runSimulation(1, 1.0, 20, 20, 1.0, 30, RandomWalkRobot))
print('3 robot, 20 x 20, 100% coverage')
print(runSimulation(3, 1.0, 20, 20, 1.0, 30, RandomWalkRobot))


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = list(range(1, 11))
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300 / width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


pos = Position(1, 1)
print(type(pos))

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
