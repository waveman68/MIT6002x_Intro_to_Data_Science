import random
import pylab


# You are given this function
def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)


# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
    - Produces a histogram of values with numBins bins and the indicated labels
    for the x and y axis
    - If title is provided by caller, puts that title on the figure and otherwise
    does not title the figure

    :type xLabel: str
    :type yLabel: str
    :type title: str
    :param values: a sequence of numbers
    :param numBins: a positive int
    :param xLabel:
    :param yLabel:
    :param title:
    """
    # TODO
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if type(title) == str:
        pylab.title(title)

    pylab.show()


# my_die = Die([1, 2, 3, 4, 5, 6, 6, 6, 7])
# distribution = []
# for i in range(100):
#     distribution.append(my_die.roll())
#
# makeHistogram(distribution, 7, 'Bin', 'Occurrence')


# Implement this -- Coding Part 2 of 2
def get_longest_run(die, trial_rolls):
    """
    Takes a list of rolls, sorts it and determines longest run

    :type trial_rolls: list
    :param die: a die object
    :param trial_rolls: list of roll results
    """
    unique_results = list(set(die.possibleVals[:]))

    if len(trial_rolls) == 0:
        return

    max_run = 0
    current_run = []
    max_roll = 0
    for r in trial_rolls:
        # compare r to last roll
        try:
            if r == current_run[-1]:
                current_run.append(r)
            else:
                current_run = [r]

        # nothing in current run gives an IndexError
        except IndexError:
            current_run.append(r)
        if len(current_run) > max_run:
            max_run = len(current_run)
            max_roll = r
    return max_roll, max_run


# d = Die([1, 2, 3, 4, 5, 6, 6, 6, 7])
# print(get_longest_run(d, [1, 4, 3]))
# print(get_longest_run(d, [1, 3, 3, 2]))
# print(get_longest_run(d, [5, 4, 4, 4, 5, 5, 2, 5]))


def getAverage(die, numRolls, numTrials):
    """
    - Calculates the expected mean value of the longest run of a number
    over numTrials runs of numRolls rolls.
    - Calls makeHistogram to produce a histogram of the longest runs for all
    the trials. There should be 10 bins in the histogram
    - Choose appropriate labels for the x and y axes.
    - Returns the mean calculated

    :type die: object
    :type numTrials: int
    :type numRolls: int
    :param die: a Die
    :param numRolls: positive int
    :param numTrials: positive int
    """
    # TODO
    assert type(die) == Die
    assert type(numRolls) == int
    assert numRolls > 0
    assert type(numTrials) == int
    assert numTrials > 0

    longest_runs = []

    for t in range(numTrials):
        rolls = []
        for n in range(numRolls):
            roll = die.roll()
            rolls.append(roll)
        if len(rolls) == 0:
            return None

        max_run = 0
        current_run = []
        for r in rolls:
            # compare r to last roll
            try:
                if r == current_run[-1]:
                    current_run.append(r)
                else:
                    current_run = [r]

            # nothing in current run gives an IndexError
            except IndexError:
                current_run.append(r)
            if len(current_run) > max_run:
                max_roll = r
                max_run = len(current_run)

        longest_runs.append(max_run)

    makeHistogram(longest_runs, 10, 'Bin', 'Number of Occurences', 'Distribution of Longest Runs')
    mean, std = getMeanAndStd(longest_runs)
    return mean


def getAverage2(die, numRolls, numTrials):
    """
    - Calculates the expected mean value of the longest run of a number
    over numTrials runs of numRolls rolls.
    - Calls makeHistogram to produce a histogram of the longest runs for all
    the trials. There should be 10 bins in the histogram
    - Choose appropriate labels for the x and y axes.
    - Returns the mean calculated

    :type die: object
    :type numTrials: int
    :type numRolls: int
    :param die: a Die
    :param numRolls: positive int
    :param numTrials: positive int
    """
    # TODO
    assert type(die) == Die
    assert type(numRolls) == int
    assert numRolls > 0
    assert type(numTrials) == int
    assert numTrials > 0

    longest_runs = []

    for n in range(numTrials):
        rolls = []
        for r in range(numRolls):
            roll = die.roll()
            rolls.append(roll)
        value, length = get_longest_run(die, rolls)
        longest_runs.append(value)

    makeHistogram(longest_runs, 10, 'Bin', 'Number of Occurences', 'Distribution of Longest Runs')
    return getMeanAndStd(longest_runs)


# One test case
print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 500, 10000))

# print(getAverage(Die([1]), 10, 1000))
# print(getAverage(Die([1,1]), 10, 1000))
# print(getAverage(Die([1, 2, 3, 4, 5, 6]), 50, 1000))
# print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 1000))
# print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 1, 10000))
