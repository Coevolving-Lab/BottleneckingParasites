'''This module takes the requested model parameters, runs the simulation across
those parameters (possibly with multiple replicates), and then pushes the data 
to logger.py. The functions in this module are generally listed in the order 
that they are called. The flow of this module is:
    1) the "run" function is called with the requested parameters. If the user
    has requested to explore a range of values for particular parameters, the
    "run" function makes sure that the model runs all possible parameter
    combinations to traverse an n-dimensional parameter space.
    2) Each unique set of parameter values is run ("run_parameter_set"). The
    starting population is initialized, then the simulation alternates between
    calculating the time until the next bottleneck occurs, processes the
    population's growth and disease spread for that amount of time, bottlenecking
    the population, and then repeating
    3) The actual timestep is processed in "run_timestep," which updates the
    values for S, I, and R according to the processes of host birth, parasite
    transmission, death, recovery, etc. Each of these processes is split into
    its own function.
    4) Finally, the "run" function tells the logger.py module to write any data
    it has accumulated to a .csv file.

The functions in this module and their descriptions:
----------------------------
run
    This is the function that is called by main.py. Runs the model across all 
    possible parameter combinations, possibly with multiple replicates. Some 
    parameters (e.g. carrying_capacity) can only have one value across all runs, 
    because it wasn't necessary or interesting for me to explore a range of 
    values for those parameters. For others, I was more interested in exploring 
    ranges. Those parameters are represented in the Parameters class 
    (in parameters.py) as lists of values, which may have a single value or 
    multiple values. The iter.product method in this function takes thoses lists 
    and returns a list of all possible combinations, which means that you can 
    vary one parameter across a range to get a one-dimensional parameter space, 
    two parameters across ranges to get a two-dimensional parameter space, etc.
log_parameter_set
    Gives the parameters and their values for this parameter set to a dataframe in the
    logger module so that the logger can make sure to fill in these columns in
    the dataframe with this "constant data", i.e. data that will be the same for
    every row.
run_parameter_set
    Runs the model such that the initial population experiences periods of
    normal population growth/parasite transmission punctuated by bottleneck 
    events.
get_time_till_bottleneck
    Returns the number of timesteps until the next bottleneck.
    This will be a whole number value. The value could be exact and 
    predetermined, or pulled from a normal distribution. This function 
    ensures that at least one timestep occurs (the bottleneck cannot happen
    instantly or at some negative value time in the past)
get_bottleneck_size
    Returns the size of the bottleneck, i.e. the number of hosts that should 
    survive through the botteneck. This size could be exact and predetermined, 
    or pulled from a normal distribution.
run_model
    Runs multiple timepoints of the model, returns the final population state,
    and logs the data generated (if not in a burn-in period).
run_timepoint
    Runs and returns the results of a single timepoint of the model. This 
    timepoint may be run in one step, or in multiple fractional steps.
get_bottleneck_survivors
    Subjects the host population to a bottleneck by sampling a number of 
    survivors from the population.
get_regulated_births
    Calculates and returns the number of new hosts that should be born in this
    timestep due to a birth process which is regulated by carrying capacity
get_exponential_births
    Calculates and returns the number of new hosts that should be born in this
    timestep due to an unregulated exponential birth process
get_s_deaths
    Calculates and returns the number of susceptible hosts that should die in
    this timestep
get_i_deaths
    Calculates and returns the number of infected hosts that should die in
    this timestep
get_r_deaths
    Calculates and returns the number of recovered hosts that should die in
    this timestep
get_ddt_infections
    Calculates and returns the number of new infections from a density-
    dependent transmission process
get_fdt_infections
    Calculates and returns the number of new infections from a frequency-
    dependent transmission process
get_recoveries
    Calculates and returns the number of infected hosts that have recovered
    in this timestep
'''

import numpy as np
import itertools as iter
from typing import Callable

import stochasticcode.logger as logger

random_number_generator = np.random.default_rng(92500169789667897205027529303633824467)
series = 1

def run(parameters) -> None:
    '''Runs the model across all possible parameter combinations. Some parameters
    (e.g. carrying_capacity) can only have one value across all runs, because it
    wasn't necessary or interesting for me to explore a range of values for those
    parameters. For others, I was more interested in exploring ranges. Those
    parameters are represented in the Parameters class (in parameters.py) as lists
    of values, which may have a single value or multiple values. The iter.product
    method in this function takes thoses lists and returns a list of all possible
    combinations, which means that you can vary one parameter across a range to
    get a one-dimensional parameter space, two parameters across ranges to get
    a two-dimensional parameter space, etc.

    parameters: an instance of the Parameters class in parameters.py
        Contains attributes which are the parameter values that the model
        should be run with. See parameters.py for more detail.
    '''

    dataframe = logger.Dataframe(file_name = parameters.file_name)

    all_parameter_sets = iter.product(parameters.initial_prevalence,
                                      parameters.bottleneck_size_mean,
                                      parameters.bottleneck_size_cv,
                                      parameters.time_till_bottleneck_mean,
                                      parameters.time_till_bottleneck_cv,
                                      parameters.host_birth_rate,
                                      parameters.parasite_fecundity_effect,
                                      parameters.s_death_rate,
                                      parameters.i_death_rate,
                                      parameters.r_death_rate,
                                      parameters.transmission_rate,
                                      parameters.recovery_rate)
    for parameter_set in all_parameter_sets:
        log_parameter_set(dataframe, parameters, parameter_set)
        run_parameter_set(dataframe, n_reps=parameters.n_reps,
                          n_bottlenecks=parameters.n_bottlenecks,
                          burn_in = parameters.burn_in,
                          initial_popsize=parameters.initial_popsize,
                          initial_prevalence=parameter_set[0],
                          bottleneck_size_mean=parameter_set[1],
                          bottleneck_size_cv=parameter_set[2],
                          time_till_bottleneck_mean=parameter_set[3],
                          time_till_bottleneck_cv=parameter_set[4],
                          host_birth_rate=parameter_set[5],
                          carrying_capacity=parameters.carrying_capacity,
                          birth_function=parameters.birth_function,
                          parasite_fecundity_effect=parameter_set[6],
                          s_death_rate=parameter_set[7],
                          i_death_rate=parameter_set[8],
                          r_death_rate=parameter_set[9],
                          transmission_rate=parameter_set[10],
                          transmission_function=parameters.transmission_function,
                          recovery_rate=parameter_set[11],
                          fractional_timestep_size=parameters.fractional_timestep_size)
        dataframe.write_data()
        
def log_parameter_set(dataframe, parameters, parameter_set: list) -> None:
    '''Gives the parameters and their values for this parameter set to the
    logger module so that the logger can make sure to fill in these columns in
    the dataframe with this "constant data", i.e. data that will be the same for
    every row.

    dataframe: an instance of the Dataframe class from logger.py
        Stores the data as it comes in from the simulation and contains methods
        to write data to .csv files in the output folder
    parameters: an instance of the Parameter class from parameters.py
        Contains, as attributes, parameter values that should be the same across
        all runs of all parameter sets. For instance, parameters.carrying_capacity
        isn't permitted to have a range of values across multiple model runs. 
        See parameters.py for more detail.
    parameter_set: list
        A list of parameter values that correspond to parameters that are 
        permitted to be explored across a range of values. This set is one such
        combination of rangeable parameters. The order of the parameter values
        in this list corresponds to the order that they are put into the 
        iter.product method in the "run" function above.
    '''
    
    constant_data = {"InitialPrevalence": parameter_set[0],
                         "BottleneckSizeMean": parameter_set[1],
                         "BottleneckSizeCV": parameter_set[2],
                         "TimeTillBottleneckMean": parameter_set[3],
                         "TimeTillBottleneckCV": parameter_set[4],
                         "BirthRate": parameter_set[5],
                         "CarryingCapacity": parameters.carrying_capacity,
                         "BirthType": parameters.birth_type,
                         "ParasiteFecundityEffect": parameter_set[6],                      
                         "SDeathRate": parameter_set[7],
                         "IDeathRate": parameter_set[8],
                         "RDeathRate": parameter_set[9],
                         "TransmissionRate": parameter_set[10],
                         "TransmissionType": parameters.transmission_type,
                         "RecoveryRate": parameter_set[11],
                         "FractTimestepSize": parameters.fractional_timestep_size}
    dataframe.add_constant_data(constant_data)

def run_parameter_set(dataframe, n_reps: int, n_bottlenecks: int, burn_in: int, 
                      initial_popsize: int, initial_prevalence: float, 
                      bottleneck_size_mean: int, bottleneck_size_cv: float, 
                      time_till_bottleneck_mean: int, 
                      time_till_bottleneck_cv: float, host_birth_rate: float, 
                      carrying_capacity: int, birth_function: Callable, 
                      parasite_fecundity_effect: float, s_death_rate: float, 
                      i_death_rate: float, r_death_rate: float,
                      transmission_rate: float, transmission_function: Callable,
                      recovery_rate: float, fractional_timestep_size: float) -> None:
    '''Runs the model such that the initial population experiences periods of
    normal population growth/parasite transmission punctuated by bottleneck 
    events.

    dataframe: an instance of the Dataframe class from logger.py
        Stores the data as it comes in from the simulation and contains methods
        to write data to .csv files in the output folder
    n_reps: int
        The number of times this parameter set should be fully replicated
    n_bottlenecks: int
        The number of bottleneck events that this population experiences
    burn_in: int
        The number of bottleneck events that should occur before data starts
        being written to the .csv file.
    initial_popsize: int
        The total number of hosts that the model run will start off with
    initial_prevalence
        The proportion of initial hosts that are already infected when the model
        run begins
    bottleneck_size_mean: int
        The mean number of hosts that survive a bottleneck event
    bottleneck_size_cv: float
        The coefficient of variation for bottleneck size. If zero, then all 
        bottlenecks are exactly of size bottleneck_size_mean
    time_till_bottleneck_mean: int
        The mean number of timesteps the model will run for until the next 
        bottleneck occurs
    time_till_bottleneck_cv: float
        The coefficient of variation for bottleneck timing. If zero, then every 
        bottleneck will occur after the model runs for 
        time_till_bottleneck_mean timesteps
    host_birth_rate: float
        The inherent birth rate of the host, which indicates the number of births
        per host per timestep.
    carrying_capacity: int
        The maximum number of hosts that the population can support. Often
        represented by K in the literature.
    birth_function: Callable
        Will either be the function get_regulated_births or get_exponential_births
        (see below)
    parasite_fecundity_effect: float
        The amount by which birth rate is lowered in infected hosts versus
        susceptible/recovered hosts. Ranges from 0 to 1, where 0 is no effect 
        (infected hosts have the same birth rate) and 1 is total sterilization
        of infected hosts
    s_death_rate: float
        The number of deaths per susceptible host per timestep.
    i_death_rate: float
        The number of deaths per infected host per timestep.
    r_death_rate: float
        The number of deaths per recovered host per timestep.
    transmission_rate: float
        The number of new infections per contact (between a susceptible and
        infected host) per timestep. Often represented by beta in the literature. 
    transmission_function: Callable
        Will either be the function get_ddt_infections or get_fdt_infections
        (see below)
    recovery_rate: float
        The number of recoveries (conversion from I to R) per infected host per
        timestep. Often represented by gamma in the literature
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many
        substeps to improve accuracy. The value is the size of the timestep, so
        a value of 0.1 means that the timestep will be run in 10 substeps of size 
        0.1
    '''    
    print(f"Bottleneck Size Mean: {bottleneck_size_mean}")
    print(f"Bottleneck Size CV: {bottleneck_size_cv}")

    for rep in range(n_reps):
        i = initial_popsize * initial_prevalence
        s = initial_popsize - i
        r = 0

        for n in range(n_bottlenecks):
            is_logging = (n >= burn_in)
            time_till_bottleneck = get_time_till_bottleneck(time_till_bottleneck_mean,
                                                            time_till_bottleneck_cv)
            s, i, r = run_model(dataframe, rep, is_logging, time_till_bottleneck, 
                                fractional_timestep_size, s, i, r, birth_function, 
                                host_birth_rate, carrying_capacity, 
                                parasite_fecundity_effect, transmission_function, 
                                transmission_rate, s_death_rate, i_death_rate, 
                                r_death_rate, recovery_rate)
            bottleneck_size = get_bottleneck_size(s, i, r, bottleneck_size_mean,
                                                bottleneck_size_cv)
            s, i, r = get_bottleneck_survivors(s, i, r, bottleneck_size)
    
def get_time_till_bottleneck(time_till_bottleneck_mean: int,
                             time_till_bottleneck_cv: float) -> int:
    '''This function returns the number of timesteps until the next bottleneck.
    This will be a whole number value. The value could be exact and 
    predetermined, or pulled from a normal distribution. This function ensures
    that the value returned is nonnegative and nonzero, simply by setting the 
    initial value to zero and resampling until it pulls a positive number. This
    should only take one try in a majority of cases but may take a couple tries
    if the mean is very low and the variance is high.
     
    time_till_bottleneck_mean: int
        The mean number of timesteps until the next bottleneck occurs
    time_till_bottleneck_cv: float
        The coefficient of variation for bottleneck timing. If zero, then every 
        bottleneck will occur after time_till_bottleneck_mean timepoints

    Returns time_till_bottleneck: int
        The number of timesteps until the next bottleneck. Will be a whole
        number greater than 0
    '''

    if time_till_bottleneck_cv == 0:
        return time_till_bottleneck_mean
    
    standard_deviation = time_till_bottleneck_cv * time_till_bottleneck_mean
    variance = standard_deviation**2

    #In the gamma distribution, mean = alpha*beta and variance = alpha*beta*beta, therefore:
    beta = variance/time_till_bottleneck_mean
    alpha = time_till_bottleneck_mean/beta
    time_till_bottleneck = round(np.random.gamma(alpha, beta))
    if time_till_bottleneck == 0:
        return 1
    return time_till_bottleneck


def get_bottleneck_size(s: float, i: float, r: float, bottleneck_size_mean: int, 
                        bottleneck_size_cv: float) -> int:
    '''This function returns the size of the bottleneck, i.e. the number of hosts that should make
    it through the botteneck. This size could be exact and predetermined, or
    pulled from a normal distribution. This function ensures
    that the value returned is equal to or less than the number of individuals
    currently in the popuation (i.e., individuals cannot be "created" in the
    bottleneck process).

    s: float
        The number of susceptible hosts in this timestep
    i: float
        The number of infected hosts in this timestep
    r: float
        The number of recovered hosts in this timestep
    bottleneck_size_mean: int
        The mean number of hosts that survive this bottleneck
    bottleneck_size_cv: float
        The coefficient of variation for bottleneck size. If zero, then all 
        bottlenecks are exactly of size bottleneck_size_mean

    Returns bottleneck_size: int
        The number of hosts that survive this bottleneck
    '''

    if bottleneck_size_cv == 0:
        return bottleneck_size_mean
    
    standard_deviation = bottleneck_size_cv * bottleneck_size_mean
    variance = standard_deviation**2

    #In the gamma distribution, mean = alpha*beta and variance = alpha*beta*beta, therefore:
    beta = variance/bottleneck_size_mean
    alpha = bottleneck_size_mean/beta
    total_pop_size = s + i + r
    bottleneck_size = total_pop_size * 10 #starting out with an absurdly high value
    while bottleneck_size > total_pop_size:
        bottleneck_size = round(np.random.gamma(alpha, beta))
    if bottleneck_size == 0:
        return 1

    return bottleneck_size


def run_model(dataframe, current_rep: int, is_logging: bool, n_timepoints: int, 
              fractional_timestep_size: float, s: int, i: int, r: int, 
              birth_function: Callable, host_birth_rate: float, 
              carrying_capacity: int, parasite_fecundity_effect: float, 
              transmission_function: Callable, transmission_rate: float, 
              s_death_rate: float, i_death_rate: float, r_death_rate: float, 
              recovery_rate: float) -> tuple[int]:
    '''Runs multiple timepoints of the model, returns the final population state,
    and (possibly) logs the data generated.

    dataframe: an instance of the Dataframe class from logger.py
        Stores the data as it comes in from the simulation and contains methods
        to write data to .csv files in the output folder
    current_rep: int
        The number of the current replicate the simulation is processing
    is_logging: bool
        If True, the data generated from this run will be added to the master
        dataframe that is written to a .csv file. If False, the data generated
        from this run will not be written (e.g. if running the model during a 
        burn-in period)
    n_timepoints: int
        The number of timepoints the model will be run for
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many
        substeps to improve accuracy. The value is the size of the timestep, so
        a value of 0.1 means that the timestep will be run in 10 substeps of size 
        0.1
    s: int
        The number of susceptible hosts in this timestep
    i: int
        The number of infected hosts in this timestep
    r: int
        The number of recovered hosts in this timestep
    birth_function: Callable
        Will either be the function get_regulated_births or get_exponential_births
        (see below)
    host_birth_rate: float
        The inherent birth rate of the host, which indicates the number of new
        births per host per timestep.
    carrying_capacity: int
        The maximum number of hosts that the population can support. Often
        represented by K in the literature.
    parasite_fecundity_effect: float
        The amount by which birth rate is lowered in infected hosts versus
        susceptible/recovered hosts. Ranges from 0 to 1, where 0 is no effect 
        (infected hosts have the same birth rate) and 1 is total sterilization
        of infected hosts
    transmission_function: Callable
        Will either be the function get_ddt_infections or get_fdt_infections
        (see below)
    transmission_rate: float
        The number of new infections per contact (between a susceptible and 
        infected host) per timestep. Often represented by beta in the literature.
    s_death_rate: float
        The number of deaths per susceptible host per timestep.
    i_death_rate: float
        The number of deaths per infected host per timestep.
    r_death_rate: float
        The number of deaths per recovered host per timestep.
    recovery_rate: float
        The number of recoveries (conversion from I to R) per infected host per
        timestep. Often represented by gamma in the literature

    Returns tuple[int]
        The first element is s, the updated number of susceptible hosts after
        running these timesteps. The second element is i, the updated number of 
        infected hosts after running these timesteps. The third element is r, 
        the updated number of recovered hosts after running these timesteps.
    '''
    
    global series

    new_data = []
    new_data.append([current_rep, series, 0, s, i, r])

    for timepoint in range(int(n_timepoints)):
        s, i, r = run_timepoint(fractional_timestep_size, s, i, r, birth_function,
                                host_birth_rate, carrying_capacity, 
                                parasite_fecundity_effect, transmission_function,
                                transmission_rate, s_death_rate, i_death_rate,
                                r_death_rate, recovery_rate)
       
        new_data.append([current_rep, series, timepoint+1, s, i, r])
    
    dataframe.log_data(is_logging, new_data)
    series += 1
    return s, i, r

def run_timepoint(fractional_timestep_size: float, s: int, i: int, r: int,
                  birth_function: Callable, host_birth_rate: float,
                  carrying_capacity: int, parasite_fecundity_effect: float,
                  transmission_function: Callable, transmission_rate: float,
                  s_death_rate: float, i_death_rate: float, r_death_rate: float,
                  recovery_rate: float) -> tuple[int]:
    '''Runs and returns the results of a single timepoint of the model. This 
    timepoint may be run in one step, or in multiple fractional steps.

    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many
        substeps to improve accuracy. The value is the size of the timestep, so
        a value of 0.1 means that the timestep will be run in 10 substeps of size 
        0.1
    s: int
        The number of susceptible hosts in this timestep
    i: int
        The number of infected hosts in this timestep
    r: int
        The number of recovered hosts in this timestep
    birth_function: Callable
        Will either be the function get_regulated_births or get_exponential_births
        (see below)
    host_birth_rate: float
        The inherent birth rate of the host, which indicates the number of new
        births per host per timestep.
    carrying_capacity: int
        The maximum number of hosts that the population can support. Often
        represented by K in the literature.
    parasite_fecundity_effect: float
        The amount by which birth rate is lowered in infected hosts versus
        susceptible/recovered hosts. Ranges from 0 to 1, where 0 is no effect 
        (infected hosts have the same birth rate) and 1 is total sterilization
        of infected hosts
    transmission_function: Callable
        Will either be the function get_ddt_infections or get_fdt_infections
        (see below)
    transmission_rate: float
        The number of new infections per contact (between a susceptible and 
        infected host) per timestep. Often represented by beta in the literature.
    s_death_rate: float
        The number of deaths per susceptible host per timestep.
    i_death_rate: float
        The number of deaths per infected host per timestep.
    r_death_rate: float
        The number of deaths per recovered host per timestep.
    recovery_rate: float
        The number of recoveries (conversion from I to R) per infected host per
        timestep. Often represented by gamma in the literature

    Returns tuple[int]
        The first element is s, the updated number of susceptible hosts after
        running this timestep. The second element is i, the updated number of 
        infected hosts after running this timestep. The third element is r, the
        updated number of recovered hosts after running this timestep.
    '''

    for _ in range(int(1 / fractional_timestep_size)):
        new_births = birth_function(s, i, r, host_birth_rate, carrying_capacity, 
                                    parasite_fecundity_effect,
                                    fractional_timestep_size)
        new_infections = transmission_function(s, i, r, transmission_rate, 
                                                fractional_timestep_size)
        new_s_deaths = get_s_deaths(s, s_death_rate, fractional_timestep_size)
        new_i_deaths = get_i_deaths(i, i_death_rate, fractional_timestep_size)
        new_r_deaths = get_r_deaths(r, r_death_rate, fractional_timestep_size)
        new_recoveries = get_recoveries(i, recovery_rate, fractional_timestep_size)

        s = s + new_births - new_infections - new_s_deaths
        i = i + new_infections - new_i_deaths - new_recoveries
        r = r - new_r_deaths + new_recoveries
    
    return (s, i, r)


def get_bottleneck_survivors(s: float, i: float, r: float, 
                             bottleneck_size: int) -> tuple[int]:
    '''Subjects the host population to a bottleneck by sampling a subset of
    hosts from the population. In the code, the numpy random number generator
    pulls from a binomial distribution to determine the number of surviving hosts
    that are infected, based on the parasite prevalence at the time of the
    bottleneck. If were no recovered individuals pre-bottleneck, then the 
    remaining hosts must be susceptible. If there were recovered individuals pre-
    bottleneck, then the code pulls from another binomial distribution to determine
    the final split between susceptible and recovered hosts.
    
    s: float
        The number of susceptible hosts in this timestep
    i: float
        The number of infected hosts in this timestep
    r: float
        The number of recovered hosts in this timestep
    bottleneck_size: int
        The number of hosts that should survive the bottleneck
    
    Returns tuple(int, int, int)
        The first element is the updated value for s, the number of susceptible
        hosts. The second element is the updated value for i, the number of
        infected hosts. The third element is the updated value for r, the
        number of recovered hosts.
    '''
    pop_size = s + i + r
    s_frequency = s / pop_size
    i_frequency = i / pop_size
    r_frequency = r / pop_size

    #Find Is first
    new_i = random_number_generator.binomial(n = bottleneck_size,
                                             p = i_frequency)
    remainder = bottleneck_size - new_i
    
    if r_frequency == 0:
        new_s = remainder
        new_r = 0
    
    else:
        new_s = random_number_generator.binomial(n = remainder,
                                                 p = s_frequency)
        new_r = remainder - new_s

    return new_s, new_i, new_r


def get_regulated_births(s: float, i: float, r: float, host_birth_rate: float,
                        carrying_capacity: int, parasite_fecundity_effect: float,
                        fractional_timestep_size: float) -> float:
    '''Calculates and returns the number of new hosts that should be born in this
    timestep due to a birth process which is regulated by carrying capacity

    s: float
        The number of susceptible hosts in this timestep
    i: float
        The number of infected hosts in this timestep
    r: float
        The number of recovered hosts in this timestep
    host_birth_rate: float
        The inherent birth rate of the host, which indicates the proportion of
        hosts per timestep that should reproduce
    carrying_capacity: int
        The maximum number of hosts that the population can support. Often
        represented by K in the literature.
    parasite_fecundity_effect: float
        The amount by which birth rate is lowered in infected hosts versus
        susceptible/recovered hosts. Ranges from 0 to 1, where 0 is no effect 
        (infected hosts have the same birth rate) and 1 is total sterilization
        of infected hosts
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many tiny
        timesteps to improve accuracy

    Returns float
        The number of new births this timestep
    '''

    population_size = s + i + r
    
    birth_rate_multiplier = (carrying_capacity - population_size) / carrying_capacity
    if birth_rate_multiplier < 0:
        birth_rate_multiplier = 0
    effective_birth_rate = host_birth_rate * birth_rate_multiplier
    infected_birth_rate = effective_birth_rate * (1 - parasite_fecundity_effect)

    births_from_s = s * effective_birth_rate
    births_from_i = i * infected_birth_rate
    births_from_r = r * effective_birth_rate
    total_births = (births_from_s + births_from_i + births_from_r) * fractional_timestep_size

    return total_births

def get_exponential_births(s: float, i: float, r: float, host_birth_rate: float,
                        carrying_capacity: int, parasite_fecundity_effect: float,
                         fractional_timestep_size: float) -> float:
    '''Calculates and returns the number of new hosts that should be born in this
    timestep due to an unregulated exponential birth process

    s: float
        The number of susceptible hosts in this timestep
    i: float
        The number of infected hosts in this timestep
    r: float
        The number of recovered hosts in this timestep
    host_birth_rate: float
        The inherent birth rate of the host, which indicates the proportion of
        hosts per timestep that should reproduce
    carrying_capacity: int
        The maximum number of hosts that the population can support. Often
        represented by K in the literature. Not used for this calculation but 
        included here so that higher-level functions can call a birth function 
        without having to know ahead of time whether it's
        get_regulated_births or get_exponential_births
    parasite_fecundity_effect: float
        The amount by which birth rate is lowered in infected hosts versus
        susceptible/recovered hosts. Ranges from 0 to 1, where 0 is no effect 
        (infected hosts have the same birth rate) and 1 is total sterilization
        of infected hosts
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many tiny
        timesteps to improve accuracy

    Returns float
        The number of new births this timestep
    '''
    infected_birth_rate = host_birth_rate * (1 - parasite_fecundity_effect)

    births_from_s = s * host_birth_rate
    births_from_i = i * infected_birth_rate
    births_from_r = r * host_birth_rate
    total_births = (births_from_s + births_from_i + births_from_r) * fractional_timestep_size
    return total_births

def get_s_deaths(s: float, s_death_rate: float, fractional_timestep_size: float) -> float:
    '''Calculates and returns the number of susceptible hosts that should die in
    this timestep

    s: float
        The number of susceptibles hosts in this timestep
    s_death_rate: float
        The proportion of susceptible hosts that die per timestep
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many tiny
        timesteps to improve accuracy

    Returns float
        The number of new S deaths this timestep
    '''
    
    return s * s_death_rate * fractional_timestep_size

def get_i_deaths(i: float, i_death_rate: float, fractional_timestep_size: float) -> float:
    '''Calculates and returns the number of infected hosts that should die in
    this timestep

    i: float
        The number of infected hosts in this timestep
    i_death_rate: float
        The proportion of infected hosts that die per timestep
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many tiny
        timesteps to improve accuracy

    Returns float
        The number of new I deaths this timestep
    '''

    return i * i_death_rate * fractional_timestep_size

def get_r_deaths(r: float, r_death_rate: float, fractional_timestep_size: float) -> float:
    '''Calculates and returns the number of recovered hosts that should die in
    this timestep

    r: float
        The number of recovered hosts in this timestep
    r_death_rate: float
        The proportion of recovered hosts that die per timestep
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many tiny
        timesteps to improve accuracy

    Returns float
        The number of new R deaths this timestep
    '''

    return r * r_death_rate * fractional_timestep_size

def get_ddt_infections(s: float, i: float, r: float, transmission_rate: float, 
                       fractional_timestep_size: float) -> float:
    '''Calculates and returns the number of new infections from a density-
    dependent transmission process

    s: float
        The number of susceptivle hosts in this timestep
    i: float
        The number of infected hosts in this timestep
    r: float
        The number of recovered hosts in this timestep. Not used for this
        calculation but included here so that the higher-level function 
        "run_model" can call a transmission function without having to know 
        ahead of time whether it's get_ddt_infections or get_fdt_infections
    transmission_rate: float
        The proportion of contacts that result in new infections in this timestep.
        Often represented by beta in the literature
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many tiny
        timesteps to improve accuracy

    Returns float
        The number of new infections from density-dependent transmission
    '''

    n_contacts = s * i
    return n_contacts * transmission_rate * fractional_timestep_size

def get_fdt_infections(s: float, i: float, r: float, transmission_rate: float,
                       fractional_timestep_size: float) -> float:
    '''Calculates and returns the number of new infections from a frequency-
    dependent transmission process

    s: float
        The number of susceptivle hosts in this timestep
    i: float
        The number of infected hosts in this timestep
    r: float
        The number of recovered hosts in this timestep
    transmission_rate: float
        The proportion of contacts that result in new infections in this timestep.
        Often represented by beta in the literature
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many tiny
        timesteps to improve accuracy

    Returns float
        The number of new infections from frequency-dependent transmission
    '''

    n_contacts = s * i
    pop_size = s + i + r
    scaled_contacts = n_contacts / pop_size
    return scaled_contacts * transmission_rate * fractional_timestep_size

def get_recoveries(i: float, recovery_rate: float, fractional_timestep_size: float) -> float:
    '''Calculates and returns the number of infected hosts that have recovered
    in this timestep

    i: float
        The number of infected hosts in this timestep
    recovery_rate: float
        The rate at which infected hosts recover from the disease and convert to
        R (recovered) hosts. Often represented by gamma in the literature
    fractional_timestep_size: float
        A value between 0 and 1 that allows the simulation to be run in many tiny
        timesteps to improve accuracy

    Returns float
        The number of new recovered hosts, which will ultimately be removed from 
        I and added to R
    '''

    return i * recovery_rate * fractional_timestep_size