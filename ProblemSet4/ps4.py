# 6.00.2x Problem Set 4

# import numpy
# import random
import pylab as pl
from ps3b import *

# from ps3b import *


# set line width
pl.rcParams['lines.linewidth'] = 6
# set font size for titles
pl.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pl.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pl.rcParams['xtick.major.size'] = 5
# set size of numbers on y-axis
pl.rcParams['ytick.major.size'] = 5
# set size of numbers on y-axis
pl.rcParams['axes.grid'] = True


def simulation_with_drug_delay(numViruses, maxPop, maxBirthProb, clearProb,
                               resistances, mutProb, numTrials, delay):
    # type: (int, int, float, float, dict, float, int) -> None
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    :param numViruses: number of ResistantVirus to create for patient (an integer)
    :param maxPop: maximum virus population for patient (an integer)
    :param maxBirthProb: Maximum reproduction probability (a float between 0-1)
    :param clearProb: maximum clearance probability (a float between 0-1)
    :param resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    :param mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    :param numTrials: number of simulation runs to execute (an integer)
    """

    # random.seed(0)
    time_steps = delay + 150
    final_virus_population = []  # a list of patient virus populations

    # virus_population = [0.0 for i in xrange(time_steps)]
    # resistant_virus_pop = [0.0 for i in xrange(time_steps)]

    for n in range(numTrials):
        # set up initial virus list for each trial/patient
        virus_list = [ResistantVirus(maxBirthProb, clearProb, resistances,
                                     mutProb) for j in xrange(numViruses)]
        my_patient = TreatedPatient(virus_list, maxPop)
        final_pop = 0

        for k in range(time_steps):
            if k == delay:
                my_patient.addPrescription('guttagonol')
            step_data = my_patient.update()
            if k == time_steps - 1:
                final_pop = step_data
        final_virus_population.append(final_pop)

    print(final_virus_population)
    return final_virus_population


def simulation_with_2drug_delay(numViruses, maxPop, maxBirthProb, clearProb,
                                resistances, mutProb, numTrials, delay):
    # type: (int, int, float, float, dict, float, int) -> None
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    :param numViruses: number of ResistantVirus to create for patient (an integer)
    :param maxPop: maximum virus population for patient (an integer)
    :param maxBirthProb: Maximum reproduction probability (a float between 0-1)
    :param clearProb: maximum clearance probability (a float between 0-1)
    :param resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    :param mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    :param numTrials: number of simulation runs to execute (an integer)
    """

    # random.seed(0)
    time_steps = delay + 300
    final_virus_population = []  # a list of patient virus populations

    # virus_population = [0.0 for i in xrange(time_steps)]
    # resistant_virus_pop = [0.0 for i in xrange(time_steps)]

    for n in range(numTrials):
        # set up initial virus list for each trial/patient
        virus_list = [ResistantVirus(maxBirthProb, clearProb, resistances,
                                     mutProb) for j in xrange(numViruses)]
        my_patient = TreatedPatient(virus_list, maxPop)
        final_pop = 0

        for k in range(time_steps):
            if k == 150:
                my_patient.addPrescription('guttagonol')
            if k == 150 + delay:
                my_patient.addPrescription('grimpex')
            step_data = my_patient.update()
            if k == time_steps - 1:
                final_pop = step_data
        final_virus_population.append(final_pop)

    print(final_virus_population)
    return final_virus_population


# simulation_with_drug_delay(numViruses=100, maxPop=1000, maxBirthProb=0.2,
#                            clearProb=0.05, resistances={"guttagonol": False},
#                            mutProb=0.005, numTrials=100, delay=75)

#
# PROBLEM 1
#


def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    # TODO 1
    delay_0 = simulation_with_drug_delay(numViruses=100, maxPop=1000,
                                         maxBirthProb=0.1, clearProb=0.05,
                                         resistances={"guttagonol": False},
                                         mutProb=0.005, numTrials=numTrials,
                                         delay=0)
    delay_75 = simulation_with_drug_delay(numViruses=100, maxPop=1000,
                                          maxBirthProb=0.1, clearProb=0.05,
                                          resistances={"guttagonol": False},
                                          mutProb=0.005, numTrials=numTrials,
                                          delay=75)
    delay_150 = simulation_with_drug_delay(numViruses=100, maxPop=1000,
                                           maxBirthProb=0.1, clearProb=0.05,
                                           resistances={"guttagonol": False},
                                           mutProb=0.005, numTrials=numTrials,
                                           delay=150)
    delay_300 = simulation_with_drug_delay(numViruses=100, maxPop=1000,
                                           maxBirthProb=0.1, clearProb=0.05,
                                           resistances={"guttagonol": False},
                                           mutProb=0.005, numTrials=numTrials,
                                           delay=300)

    fig = pl.figure(figsize=(8, 6))
    pl.subplot(221)
    pl.hist(delay_0, bins=11)
    pl.title('Simulated Total Population after Delay 0')
    pl.xlabel('Population Bin')
    pl.ylabel('# Patients')
    # pl.grid()

    pl.subplot(222)
    pl.hist(delay_75, bins=11)
    pl.title('Simulated Total Population after Delay 75')
    pl.xlabel('Population Bin')
    pl.ylabel('# Patients')
    # pl.grid()

    pl.subplot(223)
    pl.hist(delay_150, bins=11)
    pl.title('Simulated Total Population after Delay 150')
    pl.xlabel('Population Bin')
    pl.ylabel('# Patients')
    # pl.grid()

    pl.subplot(224)
    pl.hist(delay_300, bins=11)
    pl.title('Simulated Total Population after Delay 300')
    pl.xlabel('Population Bin')
    pl.ylabel('# Patients')
    # pl.grid()

    fig.set_size_inches(8, 6)
    pl.show()


# simulationDelayedTreatment(100)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO 2
    delay_0 = simulation_with_drug_delay(numViruses=100, maxPop=1000,
                                         maxBirthProb=0.1, clearProb=0.05,
                                         resistances={"guttagonol": False,
                                                      "grimpex": False},
                                         mutProb=0.01, numTrials=numTrials,
                                         delay=0)
    delay_75 = simulation_with_drug_delay(numViruses=100, maxPop=1000,
                                          maxBirthProb=0.1, clearProb=0.05,
                                          resistances={"guttagonol": False,
                                                       "grimpex": False},
                                          mutProb=0.01, numTrials=numTrials,
                                          delay=75)
    delay_150 = simulation_with_drug_delay(numViruses=100, maxPop=1000,
                                           maxBirthProb=0.1, clearProb=0.05,
                                           resistances={"guttagonol": False,
                                                        "grimpex": False},
                                           mutProb=0.01, numTrials=numTrials,
                                           delay=150)
    delay_300 = simulation_with_drug_delay(numViruses=100, maxPop=1000,
                                           maxBirthProb=0.1, clearProb=0.05,
                                           resistances={"guttagonol": False,
                                                        "grimpex": False},
                                           mutProb=0.01, numTrials=numTrials,
                                           delay=300)

    pl.figure()
    pl.subplot(221)
    pl.hist(delay_0, bins=11)
    pl.title('Simulated Total Population after Delay 0')
    pl.xlabel('Population Bin')
    pl.ylabel('# Patients')

    pl.subplot(222)
    pl.hist(delay_75, bins=11)
    pl.title('Simulated Total Population after Delay 75')
    pl.xlabel('Population Bin')
    pl.ylabel('# Patients')

    pl.subplot(223)
    pl.hist(delay_150, bins=11)
    pl.title('Simulated Total Population after Delay 150')
    pl.xlabel('Population Bin')
    pl.ylabel('# Patients')

    pl.subplot(224)
    pl.hist(delay_300, bins=11)
    pl.title('Simulated Total Population after Delay 300')
    pl.xlabel('Population Bin')
    pl.ylabel('# Patients')

    pl.show()

simulationTwoDrugsDelayedTreatment(100)
