import math
import random
import pylab


def simWalks(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances


def sim_walks_xy(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0, 0)
    x_locations = []
    y_locations = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        end_location = walkVector(f, homer, numSteps)
        x_locations.append(end_location[0])
        y_locations.append(end_location[1])
    return x_locations, y_locations


class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name


def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return (f.getLoc(d).getX() - start.getX(),
            f.getLoc(d).getY() - start.getY())


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = \
            [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = \
            [(0.0, 0.9), (0.0, -1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)


class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))


class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices = \
            [(0.0, 0.5), (0.0, -0.5),
             (1.5, 0.0), (-1.5, 0.0)]
        return random.choice(stepChoices)


class DDrunk(Drunk):
    def takeStep(self):
        stepChoices = \
            [(0.85, 0.85), (-0.85, -0.85),
             (-0.56, 0.56), (0.56, -0.56)]
        return random.choice(stepChoices)

def drunkTestP(numTrials=50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    distances = simWalks(numSteps, numTrials, dClass)
    pylab.plot(stepsTaken, meanDistances,
               label=dClass.__name__)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend(loc='upper left')
    pylab.show()


# drunkTestP()

def drunkTestP2(numTrials=1000):
    numSteps = 1000
    x, y = sim_walks_xy(numSteps, numTrials, EDrunk)
    pylab.scatter(x, y)
    pylab.xlim((-100, 100))
    pylab.ylim((-100, 100))
    pylab.title('Distribution of Final Positions')
    pylab.xlabel('x')
    pylab.ylabel('y')
    pylab.show()


drunkTestP2()
