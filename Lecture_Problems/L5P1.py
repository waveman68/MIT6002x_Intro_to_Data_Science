import random


def pick_ball(bucket):
    """
    Randomly pick a ball from a bucket of green and red balls, initially 3 & 3
    :type bucket: list
    :param bucket: Bucket of up to 6 balls
    """
    return random.randint(0, len(bucket) - 1)


def noReplacementSimulation(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    :type numTrials: int
    """
    trials = []

    for i in range(numTrials):
        # bucket of 3 red (0) and 3 green (1) balls
        bucket = [0, 0, 0, 1, 1, 1]
        # track the balls picked per trial in a list
        trial = []

        for ball in range(3):
            # pick 3 balls and remove them from the list
            trial.append(bucket.pop(pick_ball(bucket)))

        # track if all balls are the same color
        if trial[0] == trial[1] and trial[1] == trial[2]:
            trials.append(1)  # all balls the same color
        else:
            trials.append(0)  # 1 doesn't match the others

    # using the number coding allows for a simple calculation of the fraction
    return sum(trials) / float(len(trials))


print(noReplacementSimulation(10000))
