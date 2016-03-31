# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics

import random
import pylab
from ps3b_precompiled_27 import *

# set line width
pylab.rcParams['lines.linewidth'] = 6
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
# set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5

"""
Begin helper code
"""


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


"""
End helper code
"""


#
# PROBLEM 2
#


class SimpleVirus2(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        :type maxBirthProb: float
        :type clearProb: float
        :param maxBirthProb: Maximum reproduction probability (a float between 0-1)
        :param clearProb: Maximum clearance probability (a float between 0-1).
        """
        # TODO P2.1: DONE __init__ SimpleVirus

        assert 0 <= maxBirthProb <= 1
        assert 0 <= clearProb <= 1
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        :rtype: float
        """
        # TODO P2.2: DONE getter maxBirthProb

        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        # TODO P2.3: DONE getter clearProb

        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        # TODO P2.9: DONE doesClear method
        cleared = random.random()
        if cleared <= self.getClearProb():
            return True
        else:
            return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # TODO P2.4 DONE? reproduce return a new instance

        reproduce_probability = self.maxBirthProb * (1 - popDensity)

        if random.random() < reproduce_probability:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException('Virus did not reproduce')


class Patient2(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        :type viruses: list
        :type maxPop: int
        :param viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        :param maxPop: the maximum virus population for this patient (an integer)
        """

        # TODO P2.5: DONE __init__ Patient
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        # TODO P2.6: DONE getter viruses
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        # TODO P2.7: DONE getter maxPop
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        returns: The total virus population (an integer)
        :rtype: int
        """

        # TODO P2.10: DONE get total virus population method
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        :rtype: int
        """

        # TODO P2.8: DONE implement Patient update method
        clear_viruses = self.viruses[:]
        for v in clear_viruses:
            if v.doesClear():
                self.viruses.remove(v)

        reproduce_viruses = self.viruses[:]
        population_density = self.getTotalPop() / float(self.maxPop)
        for v in reproduce_viruses:
            try:
                new_v = v.reproduce(population_density)
                self.viruses.append(new_v)
            except NoChildException:
                pass

        return len(self.viruses)


#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 time-steps, and plots the average virus population size as a
    function of time.

    :param numViruses:  number of SimpleVirus to create for patient
                        (an integer)
    :param maxPop:      maximum virus population for patient (an integer)
    :param maxBirthProb: Maximum reproduction probability
                            (a float between 0-1)
    :param clearProb:   Maximum clearance probability (a float between 0-1)
    :param numTrials:   number of simulation runs to execute (an integer)
    """

    # TODO 3.1 Run/analyze simple simulation
    time_steps = 300
    time_array = range(time_steps)
    patients_w_o_drugs = []  # number of patients = number of trials

    virus_population = []

    for n in range(numTrials):
        # set up initial virus list for each trial/patient
        virus_list = []
        for i in range(numViruses):
            virus_list.append(SimpleVirus2(maxBirthProb, clearProb))
        patients_w_o_drugs.append(Patient2(virus_list, maxPop))

    # store virus population for each time step

    for i in range(time_steps):
        step_data = 0
        for n in range(numTrials):
            step_data += patients_w_o_drugs[n].update()
        step_data /= float(numTrials)
        virus_population.append(step_data)

    pylab.figure()
    pylab.plot(time_array, virus_population)
    pylab.title('SimpleVirus simulation')
    pylab.legend()
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.show()


# simulationWithoutDrug(100, 1000, 0.1, 0.05, 10)


#
# PROBLEM 4
#
class ResistantVirus2(SimpleVirus2):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb:

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb:
        :type maxBirthProb: float
        :type clearProb: float
        :type resistances: dict
        :type mutProb: float
        :param maxBirthProb: Maximum reproduction probability (a float between 0-1)
        :param clearProb:
        :param resistances:
        :param mutProb: Mutation probability for this virus particle (a float). This is
                        the probability of the offspring acquiring or losing resistance to a drug.
        :rtype: object
        """
        # TODO 4.1: DONE initialize

        SimpleVirus2.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        :rtype: dict
        """
        # TODO 4.2: DONE getter
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        # TODO 4.3: DONE getter
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        :type drug: str
        :param drug: The drug (a string)
        :rtype: bool
        """
        # TODO 4.4 DONE: look up resistance
        try:
            return self.resistances[drug]
        except KeyError:
            return False

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:

        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        :rtype: object
        :return: a new instance of the ResistantVirus class representing the
            offspring of this virus particle. The child should have the same
            maxBirthProb and clearProb values as this virus. Raises a
            NoChildException if this virus particle does not reproduce.
        :type activeDrugs: list
        :param activeDrugs: a list of the drug names acting on this virus particle
                            (a list of strings).
        :type popDensity: float
        :param popDensity: the population density (a float), defined as the current
                            virus population divided by the maximum population
        """
        # TODO 4.5: DONE reproduce resistant virus

        reproduce_probability = self.maxBirthProb * (1 - popDensity)

        if random.random() < reproduce_probability:
            resistant = True
            # determine resistance to drugs applied, store as bool in resistant
            for drug in activeDrugs:
                resistant = resistant and self.isResistantTo(drug)

            if resistant:
                child_resistances = self.resistances.copy()
                if random.random() < self.mutProb:
                    for drug in child_resistances.iterkeys():
                        child_resistances[drug] = not child_resistances[drug]
                return ResistantVirus2(self.maxBirthProb, self.clearProb,
                                       child_resistances, self.mutProb)

            else:
                raise NoChildException('Virus did not reproduce')

        else:
            raise NoChildException('Virus did not reproduce')


class TreatedPatient2(Patient2):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        # TODO 4.6: DONE initialize treated patient
        Patient2.__init__(self, viruses, maxPop)
        self.drugs = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        # TODO 4.7: DONE add prescription
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        # TODO 4.8: DONE prescriptions getter
        return self.drugs

    def get_resistant_viruses(self, drug_resist):
        """
        returns: A list of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        :param drugResist: which drug resistances to include in population
        """
        resistant_viruses = []  # initialize list

        # iterate virus population and check resistance
        for v in self.viruses:
            resistant = True
            for d in drug_resist:
                resistant = resistant and v.isResistantTo(d)
            if resistant:
                resistant_viruses.append(v)

        return resistant_viruses

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO 4.9: resistant population getter
        resistant_viruses = self.get_resistant_viruses(drugResist)

        return len(resistant_viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        :rtype: int
        """
        # TODO 4.10: complete treated patient update method

        clear_viruses = self.viruses[:]
        for v in clear_viruses:
            if v.doesClear():
                try:
                    self.viruses.remove(v)
                except ValueError:
                    pass

        # only resistant viruses reproduce
        resistant_viruses = self.get_resistant_viruses(
            self.getPrescriptions())
        population_density = self.getTotalPop() / float(self.maxPop)

        # reproduce as resistant virus in presence of drugs
        for v in resistant_viruses:
            try:
                # reproduce and add virus to population
                new_v = v.reproduce(population_density, self.getPrescriptions())
                self.viruses.append(new_v)

            except NoChildException:
                pass

        return len(self.viruses)


# virus = ResistantVirus(1.0, 0.0, {}, 0.0)
# patient = TreatedPatient([virus], 100)
# for i in range(100):
#     print(patient.update())

# virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
# virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
# patient = TreatedPatient([virus1, virus2, virus3], 100)
# print(patient.getResistPop(['drug1']))
# print(patient.getResistPop(['drug2']))
# print(patient.getResistPop(['drug1', 'drug2']))
# print(patient.getResistPop(['drug3']))
# print(patient.getResistPop(['drug1', 'drug3']))
# print(patient.getResistPop(['drug1', 'drug2', 'drug3']))


#
# PROBLEM 5
#


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb,
                       resistances, mutProb, numTrials):
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
    # TODO 5.1 run and plot simulation

    # random.seed(0)
    time_steps = 300
    patients_w_drugs = []  # number of patients = number of trials

    virus_population = [0.0 for i in xrange(time_steps)]
    resistant_virus_pop = [0.0 for i in xrange(time_steps)]

    for n in range(numTrials):
        # set up initial virus list for each trial/patient
        virus_list = [ResistantVirus(maxBirthProb, clearProb, resistances,
                                     mutProb) for j in xrange(numViruses)]
        my_patient = TreatedPatient(virus_list, maxPop)

        for k in range(time_steps):
            if k == 150:
                my_patient.addPrescription('guttagonol')
            step_data = my_patient.update()
            step_data_resistant = my_patient.getResistPop(['guttagonol'])
            virus_population[k] += step_data
            resistant_virus_pop[k] += step_data_resistant

    for m in xrange(time_steps):
        virus_population[m] = float(virus_population[m]) / float(numTrials)
        resistant_virus_pop[m] = float(resistant_virus_pop[m]) / float(numTrials)

    pylab.figure()
    pylab.plot(virus_population, label='Total Virus Pop.')
    pylab.plot(resistant_virus_pop, label='Resistant Virus Pop.', color='green')
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('time step')
    pylab.ylabel('# viruses')
    pylab.legend()
    pylab.show()

    print(virus_population)
    print(resistant_virus_pop)


# def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb,
#                            resistances, mutProb, numTrials):
#
#     # type: (int, int, float, float, dict, float, int) -> None
#     """
#     Runs simulations and plots graphs for problem 5.
#
#     For each of numTrials trials, instantiates a patient, runs a simulation for
#     150 timesteps, adds guttagonol, and runs the simulation for an additional
#     150 timesteps.  At the end plots the average virus population size
#     (for both the total virus population and the guttagonol-resistant virus
#     population) as a function of time.
#
#     :param numViruses: number of ResistantVirus to create for patient (an integer)
#     :param maxPop: maximum virus population for patient (an integer)
#     :param maxBirthProb: Maximum reproduction probability (a float between 0-1)
#     :param clearProb: maximum clearance probability (a float between 0-1)
#     :param resistances: a dictionary of drugs that each ResistantVirus is resistant to
#                  (e.g., {'guttagonol': False})
#     :param mutProb: mutation probability for each ResistantVirus particle
#              (a float between 0-1).
#     :param numTrials: number of simulation runs to execute (an integer)
#     """
#     # TODO 5.1 run and plot simulation
#
#     random.seed(0)
#     time_steps = 300
#     patients_w_drugs = []  # number of patients = number of trials
#
#     for n in xrange(numTrials):
#         viruses = []
#         for j in xrange(numViruses):
#             viruses.append(ResistantVirus(maxBirthProb, clearProb,
#                                           resistances, mutProb))
#         patients_w_drugs.append(TreatedPatient(viruses, maxPop))
#
#     virus_population = []
#     resistant_virus_pop = []
#
#
#     for i in xrange(time_steps):
#         step_total_pop = 0
#         step_resistant_pop = 0
#         if i == 149:
#             for p in patients_w_drugs:
#                 p.addPrescription('guttagonol')
#         for n in xrange(numTrials):
#             step_total_pop += patients_w_drugs[n].update()
#             step_resistant_pop += patients_w_drugs[n].getResistPop(['guttagonol'])
#
#         step_total_pop = float(step_total_pop) / float(numTrials)
#         step_resistant_pop = float(step_resistant_pop) / float(numTrials)
#         virus_population.append(step_total_pop)
#         resistant_virus_pop.append(step_resistant_pop)
#
#     pylab.figure()
#     pylab.plot(virus_population, label='Total Virus Pop.')
#     pylab.plot(resistant_virus_pop, label='Resistant Virus Pop.', color='green')
#     pylab.title('ResistantVirus simulation')
#     pylab.xlabel('time step')
#     pylab.ylabel('# viruses')
#     pylab.legend()
#     pylab.show()
#
#     print(virus_population)
#     print(resistant_virus_pop)



# simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.05, 10)

# Simulation 1
# simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
# Simulation 2
# simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
# Simulation 3
simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)

# virus_list = []
# for i in range(5):
#     virus_list.append(ResistantVirus(1.0, 0.0,
#                                      {"guttagonol": True}, 1.0))
# virus_list2 = []
# for j in range(5):
#     virus_list2.append(ResistantVirus2(1.0, 0.0,
#                                        {"guttagonol": True}, 1.0))
#
# treated_patient = TreatedPatient(virus_list, 20)
# treated_patient2 = TreatedPatient2(virus_list2, 20)
# print('.pyc total pop: ', treated_patient.getTotalPop(), '   My code total pop: ', treated_patient2.getTotalPop())
#
# random.seed(0)
#
# for t in xrange(30):
#     resistance_list = []
#     for v in treated_patient.viruses:
#         resistance_list.append(v.isResistantTo('guttagonol'))
#         population_density = float(len(resistance_list)) / float(10)
#
#     resistance_list2 = []
#     for v2 in treated_patient2.viruses:
#         resistance_list2.append(v2.isResistantTo('guttagonol'))
#         population_density2 = float(len(resistance_list2)) / float(10)
#
#     print(t, '.pyc: ', len(resistance_list), treated_patient.getResistPop(['guttagonol']), resistance_list)
#     print(t, 'My code', len(resistance_list2), treated_patient2.getResistPop(['guttagonol']), resistance_list2)
#     treated_patient.update()
#     treated_patient2.update()
