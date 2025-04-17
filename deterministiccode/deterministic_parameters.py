'''This module contains a single class, Parameters, which is a convenient
container to hold model parameters and alter them. Instances of Parameters are
created in main.py. When a new Parameters instance is created, its "__init__"
method is called to populate it with default parameter values. This way, you
only need to explicitly change parameter values that differ from the defaults.

Some model parameters are "rangeable," meaning that you can tell the model to
traverse a range of values. For instance, I can have the model run with a series
of values of host_birth_rate from 0.1 to 0.5, with a step size of 0.1. Rangeable
parameters have their values stored in a list (inside square brackets), even if 
a single value is desired. This helps the model.py module calculate all possible 
combinations of rangeable parameters to generate n-dimensional parameter spaces, 
since the iter.product method from the itertools library combines lists.

Other model parameters are not rangeable and can take a single value. Which
model parameters are rangeable and which aren't is arbitrary and just reflects
the parameter spaces I wanted to explore for my own research.

The Parameters class contains several methods that help set model parameters to
non-default values. The format is that nonrangeable parameters are set 
with a single argument, e.g. parameters1.set_carrying_capacity(750). Rangeable
parameters can be set with a single argument, 
e.g. parameters1.set_host_birth_rate(0.05), or with optional max and step_size
arguments to generate a range of values, 
e.g. parameters1.set_host_birth_rate(0.05, 0.1, 0.01) will run the model for the
host_birth_rate values 0.05, 0.06, 0.07, 0.08, 0.09, and 0.1
Two methods, set_birth_function and set_transmission_function, take string
arguments to specify the type of birth ("Regulated" or "Exponential") and the
type of transmission ("Density" or "Frequency").

A description of all model parameters:
-------------------------------------

file_name: str
    The desired file name for the .csv file that will be placed in the output 
    folder.
    Not rangeable.
    Default = "data"

initial_popsize: int
    The total number of hosts that each model run will start off with.
    Not rangeable.
    Default = 1000

initial_prevalence: list[float]
    The proportion of initial hosts that are already infected when the model run 
    begins. Should be between 0 (no infection) and 1 (all hosts start out 
    infected).
    Rangeable.
    Default = [1.0]

n_bottlenecks: int
    The number of bottleneck events that the population experiences.
    Not rangeable.
    Default = 20

burn_in: int
    The number of bottleneck events that should occur before data starts being 
    written to the .csv file. Useful to give the model enough time to converge 
    before recording data. Should be less than the value for n_bottlenecks,
    otherwise no data will be written.
    Not rangeable.
    Default = 0

bottleneck_size_mean: list[int]
    The mean number of hosts that survive a bottleneck event. If the model 
    parameter bottleneck_size_cv (see below) is zero, then all bottlenecks 
    will be exactly of size bottleneck_size_mean.
    Rangeable.
    Default = [100]

bottleneck_size_cv: list[float]
    The coefficient of variation for the normal distribution of possible 
    bottleneck sizes. The CV is the standard deviation divided by the mean. This
    allows for you to explore how a given amount of variation affects the system
    across a range of bottleneck sizes. If zero, then all bottlenecks are 
    exactly of size bottleneck_size_mean (see above). 
    Rangeable.
    Default = [0]

time_till_bottleneck_mean: list[int]
    The mean number of timesteps the model will run for until the next 
    bottleneck occurs. If the model parameter time_till_bottleneck_cv (see
    below) is zero, then all bottlenecks will be exactly 
    time_till_bottleneck_mean timesteps apart.
    Rangeable.
    Default = [75]

time_till_bottleneck_cv: list[float]
    The coefficient of variation for the normal distribution of possible 
    bottleneck timing. The CV is the standard deviation divided by the mean. This
    allows for you to explore how a given amount of variation affects the system
    across a range of bottleneck timing. If zero, then every bottleneck will
    occur after the model runs for exactly time_till_bottleneck_mean timesteps
    (see above). 
    Rangeable.
    Default = [0] 

host_birth_rate: list[float]
    The inherent birth rate of the host, which indicates the proportion of hosts 
    per timestep that should reproduce.
    Rangeable.
    Default = [0.01]

carrying_capacity: int
    The maximum number of hosts that the population can support. Often 
    represented by K in the literature.
    Not rangeable.
    Default = 1000

birth_type: str
    A name that represents one of two possible methods of population growth. A
    value of "Regulated" (the default) models population growth that is
    regulated by carrying capacity. A value of "Exponential" models population
    growth that is unregulated. Trying to use any other value in the method
    set_birth_function will result in an error.
    Possible values = "Regulated", "Exponential"
    Default = "Regulated"

birth_function: Callable
    The birth function, pulled from the deterministic_model.py module, which the 
    model should run when processing births. This parameter is not manually 
    changed but the function is pulled in the set_birth_function method by 
    inputting the name of the birth type, i.e. "Regulated" or "Exponential".
    Possible values = deterministic_model.get_regulated_births, 
    deterministic_model.get_exponential_births
    Default = deterministic_model.get_regulated_births

parasite_fecundity_effect: list[float]
    The amount by which host birth rate is lowered in infected hosts versus
    susceptible/recovered hosts. Possible values run from 0 to 1, inclusive.
    0 means no effet (infected hosts have the same birth rate) while 1 is total 
    sterilization of infected hosts
    Rangeable.
    Default = 0

s_death_rate: list[float]
    The proportion of susceptible hosts that die per timestep.
    Rangeable.
    Default = 0

i_death_rate: list[float]
    The proportion of infected hosts that die per timestep.
    Rangeable.
    Default = 0

r_death_rate: list[float]
    The proportion of recovered hosts that die per timestep.
    Rangeable.
    Default = 0

transmission_rate: list[float]
    The proportion of contacts (between susceptible and infected hosts) 
    that result in new infections per timestep. Often represented by 
    beta in the literature. Note that the transmission rate is not necessarily
    the same for density-dependent transmission versus frequency-dependent
    transmission. While the default for DDT is 0.0001, this is far too low for
    FDT and should be something more like 0.05.
    Rangeable.
    Default = 0.000025

transmission_type: str
    A name that represents one of two possible methods of parasite transmission.
    A value of "Density" (the default) models density-dependent transmission. A 
    value of "Frequency" models frequency-dependent transmission. Trying to use 
    any other value in the method set_transmission_function will result in an 
    error.
    Possible values = "Density", "Frequency"
    Default = "Density"

transmission_function: Callable
    The transmission function, pulled from the deterministic_model.py module, 
    which the model should run when processing transmission. This parameter is 
    not manually changed but the function is pulled in the 
    set_transmission_function method by inputting the name of the transmission 
    type, i.e. "Density" or "Frequency".
    Possible values = deterministic_model.get_ddt_infections, 
    deterministic_model.get_fdt_infections
    Default = deterministic_model.get_ddt_infections

recovery_rate: list[float]
    The proportion of infected hosts that recover from disease (convert from I
    to R) per timestep. Often represented by gamma in the literature
    Rangeable.
    Default = 0

fractional_timestep_size: float
    A value between 0 and 1 that indicates the size of the sub-timestep that the
    simulation should use to update values. Data is only written for whole-
    number timesteps, but can be calculated through multiple iterations of 
    fractional timesteps. For instance, a value of 1 means that the between
    timesteps 3 and 4, the model is updated once. A value of 0.1 means that
    between timesteps 3 and 4, the model is actually updated 10 times, since
    the fractional timestep size is one tenth of a whole timestep. 
    Not rangeable.
    Default = 0.01
'''

import numpy as np
from typing import Callable

import deterministiccode.deterministic_model as det_model

class Parameters:
    def __init__(self) -> None:
        '''Initializes an instance of Parameters with default values. See the
        docstring above for a full explanation of all model parameters.
        Parameter values in square brackets (e.g. initial_prevalence) are
        rangeable parameters where the values appear in lists so that
        n-dimensional parameter spaces can be constructed with all possible
        combinations of parameter values.
        '''
        self.file_name: str = "data"

        self.initial_popsize: int = 1000
        self.initial_prevalence: list[float] = [1.0]

        self.n_bottlenecks: int = 20
        self.burn_in: int = 0
        self.bottleneck_size_mean: list[int] = [100]
        self.bottleneck_size_cv: list[float] = [0]
        self.time_till_bottleneck_mean: list[int] = [300]
        self.time_till_bottleneck_cv: list[float] = [0]
        
        self.host_birth_rate: list[float] = [0.01]
        self.carrying_capacity: int = 1000
        self.birth_type: str = "Regulated"
        self.birth_function: Callable = det_model.get_regulated_births
        self.parasite_fecundity_effect: list[float] = [0]
        self.s_death_rate: list[float] = [0]
        self.i_death_rate: list[float] = [0]
        self.r_death_rate: list[float] = [0]
        self.transmission_rate: list[float] = [0.000025]
        self.transmission_type: str = "Density"
        self.transmission_function: Callable = det_model.get_ddt_infections
        self.recovery_rate: list[float] = [0]
        self.fractional_timestep_size: float = 0.01

    def set_file_name(self, file_name: str) -> None:
        '''Changes the file name of the output file from its default. This
        parameter is not rangeable. Note that this function does not check
        whether the file name is a valid filename.

        file_name: str
            The desired name of the output .csv file from this run of the 
            simulation
        '''

        self.file_name = file_name
    
    def set_initial_popsize(self, initial_popsize: int) -> None:
        '''Changes the model parameter initial_popsize from its default. This 
        model parameter is not rangeable.

        initial_popsize: int
            The total number of hosts that the model run will start off with
        '''

        self.initial_popsize = initial_popsize

    def set_initial_prevalence(self, initial_prevalence: float, 
                                  max: int=0, step_size: int=0) -> None:
        '''Changes the model parameter initial_prevalence from its default.
        This model parameter is rangeable.
        
        initial_prevlance: float
            The proportion of initial hosts that are already infected when the 
            model run begins. Ranges between 0 (no infection) and 1 (all hosts
            are infected)
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is initial_prevlance
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            initial_prevlance
        '''

        self.initial_prevalence = self.get_range(initial_prevalence, max, step_size)

    def set_n_bottlenecks(self, n_bottlenecks: int) -> None:
        '''Changes the model parameter n_bottlenecks from its default. This 
        model parameter is not rangeable.
        
        n_bottlenecks: int
            The number of bottleneck events that the population experiences
        '''

        self.n_bottlenecks = n_bottlenecks
    
    def set_burn_in(self, burn_in: int) -> None:
        '''Changes the model parameter burn_in from its default. This model 
        parameter is not rangeable.

        burn_in: int
            The number of bottleneck events that should occur before data starts
            being written to the .csv file. Useful to give the model enough time
            to converge before recording data.
        '''

        self.burn_in = burn_in

    def set_bottleneck_size_mean(self, bottleneck_size_mean: int,
                                       max: int=0, step_size: int=0) -> None:
        '''Changes the model parameter bottleneck_size_mean from its 
        default. This model parameter is rangeable.
        
        bottleneck_size_mean: int
            The mean number of hosts that survive a bottleneck event. If the 
            model parameter bottleneck_size_cv is zero, then all 
            bottlenecks will be of size bottleneck_size_mean.
        max: int
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is 
            bottleneck_size_mean
        step_size: int
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            bottleneck_size_mean
        '''

        self.bottleneck_size_mean = self.get_range(bottleneck_size_mean, 
                                                   max, step_size)

    def set_bottleneck_size_cv(self, bottleneck_size_cv: float,
                               max: float=0, step_size: float=0) -> None:
        '''Changes the model parameter bottleneck_size_cv from its 
        default. This model parameter is rangeable.
        
        bottleneck_size_cv: float
            The coefficient of variation for the normal distribution of possible 
            bottleneck sizes. If zero, then all bottlenecks are exactly of size 
            bottleneck_size_mean
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is 
            bottleneck_size_cv
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            bottleneck_size_cv
        '''

        self.bottleneck_size_cv = self.get_range(bottleneck_size_cv, 
                                                 max, step_size)

    def set_time_till_bottleneck_mean(self, time_till_bottleneck_mean: int,
                                            max: int=0, step_size: int=0) -> None:
        '''Changes the model parameter time_till_bottleneck_mean from its 
        default. This model parameter is rangeable.
        
        time_till_bottleneck_mean: int
            The mean number of timesteps the model will run for until the next
            bottleneck occurs. If the model parameter 
            time_till_bottleneck_cv is zero, then all bottlenecks will be
            time_till_bottleneck_mean timesteps apart.
        max: int
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is 
            time_till_bottleneck_mean
        step_size: int
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            time_till_bottleneck_mean
        '''

        self.time_till_bottleneck_mean = self.get_range(time_till_bottleneck_mean, 
                                                        max, step_size)

    def set_time_till_bottleneck_cv(self, time_till_bottleneck_cv: float,
                                    max: float=0, step_size: float=0) -> None:
        '''Changes the model parameter time_till_bottleneck_cv from its 
        default. This model parameter is rangeable.
        
        time_till_bottleneck_cv: float
            The coefficient of variation for the normal distribution of possible 
            bottleneck timing. If zero, then every bottleneck will occur after 
            the model runs for time_till_bottleneck_mean timesteps
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is 
            time_till_bottleneck_cv
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            time_till_bottleneck_cv
        '''

        self.time_till_bottleneck_cv = self.get_range(time_till_bottleneck_cv, 
                                                      max, step_size)

    def set_host_birth_rate(self, host_birth_rate: float, 
                                  max: float=0, step_size: float=0) -> None:
        '''Changes the model parameter host_birth_rate from its default.
        This model parameter is rangeable.
        
        host_birth_rate: float
            The inherent birth rate of the host, which indicates the proportion 
            of hosts per timestep that should reproduce
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is host_birth_rate
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            host_birth_rate
        '''

        self.host_birth_rate = self.get_range(host_birth_rate, max, step_size)
        
    def set_carrying_capacity(self, carrying_capacity: int) -> None:
        '''Changes the model parameter carrying_capacity from its default.
        This model parameter is not rangeable.

        carrying_capacity: int
            The maximum number of hosts that the population can support. Often
            represented by K in the literature.
        '''

        self.carrying_capacity = carrying_capacity

    def set_birth_function(self, birth_type: str) -> None:
        '''Changes which type of host birth the model uses. Stores
        the deterministic_model.py function that corresponds to the desired type 
        of host birth.

        birth_type: str
            The only permitted values are "Regulated", to model population
            growth regulated by a carrying capacity, or "Exponential", to model
            unregulated population growth.

        Raises ValueError
            If birth_type is something other than "Regulated" or "Exponential"
        '''

        if birth_type == "Regulated":
            self.birth_type = "Regulated"
            self.birth_function = det_model.get_regulated_births
        elif birth_type == "Exponential":
            self.birth_type = "Exponential"
            self.birth_function = det_model.get_exponential_births
        else:
            raise ValueError('''The method set_birth_function in parameters.py
                                only takes birth_type="Regulated" or
                                birth_type="Exponential".''')

    def set_parasite_fecundity_effect(self, parasite_fecundity_effect: float,
                                            max: float=0, step_size: float=0) -> None:
        '''Changes the model parameter parasite_fecundity_effect from its default.
        This model parameter is rangeable. Warning: values should range between 
        0 and 1, but this is not enforced.
        
        parasite_fecundity_effect: float
            The amount by which birth rate is lowered in infected hosts versus
            susceptible/recovered hosts. Ranges from 0 to 1, where 0 is no 
            effect (infected hosts have the same birth rate) and 1 is total 
            sterilization of infected hosts
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is 
            parasite_fecundity_effect
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            parasite_fecundity_effect
        '''

        self.parasite_fecundity_effect = self.get_range(parasite_fecundity_effect, 
                                                        max, step_size)

    def set_s_death_rate(self, s_death_rate: float,
                               max: float=0, step_size: float=0) -> None:
        '''Changes the model parameter s_death_rate from its default.
        This model parameter is rangeable.
        
        s_death_rate: float
            The proportion of susceptible hosts that die per timestep
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is s_death_rate
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            s_death_rate
        '''

        self.s_death_rate = self.get_range(s_death_rate, max, step_size)

    def set_i_death_rate(self, i_death_rate: float,
                               max: float=0, step_size: float=0) -> None:
        '''Changes the model parameter i_death_rate from its default.
        This model parameter is rangeable.
        
        i_death_rate: float
            The proportion of infected hosts that die per timestep
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is i_death_rate
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            i_death_rate
        '''

        self.i_death_rate = self.get_range(i_death_rate, max, step_size)

    def set_r_death_rate(self, r_death_rate: float,
                               max: float=0, step_size: float=0) -> None:
        '''Changes the model parameter r_death_rate from its default.
        This model parameter is rangeable.
        
        r_death_rate: float
            The proportion of recovered hosts that die per timestep
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is r_death_rate
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            r_death_rate
        '''

        self.r_death_rate = self.get_range(r_death_rate, max, step_size)

    def set_transmission_rate(self, transmission_rate: float,
                              max: float=0, step_size: float=0) -> None:
        '''Changes the model parameter transmission_rate from its default.
        This model parameter is rangeable.
        
        transmission_rate: float
            The proportion of contacts (between susceptible and infected hosts) 
            that result in new infections per timestep. Often represented by 
            beta in the literature
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is transmission_rate
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is 
            transmission_rate
        '''

        self.transmission_rate = self.get_range(transmission_rate, max, step_size)

    def set_transmission_function(self, transmission_type: str) -> None:
        '''Changes which type of parasite transmission the model uses. Stores
        the deterministic_model.py function that corresponds to the desired type 
        of transmission.

        transmission_type: str
            The only permitted values are "Density", to model density-dependent
            transmission, or "Frequency", to model frequency-dependent
            transmission.

        Raises ValueError
            If transmission_type is something other than "Density" or "Frequency"
        '''

        if transmission_type == "Density":
            self.transmission_type = "Density"
            self.transmission_function = det_model.get_ddt_infections
        elif transmission_type == "Frequency":
            self.transmission_type = "Frequency"
            self.transmission_function = det_model.get_fdt_infections
        else:
            raise ValueError('''The method set_transmission_function in parameters.py
                                only takes transmission_type="Density" or
                                transmission_type="Frequency".''')

    def set_recovery_rate(self, recovery_rate: float,
                                max: float=0, step_size: float=0) -> None:
        '''Changes the model parameter recovery_rate from its default.
        This model parameter is rangeable.
        
        recovery_rate: float
            The proportion of infected hosts that recover from disease (convert
            to recovered R hosts) per timestep. Often represented by gamma in 
            the literature
        max: float
            The maximum value of the desired parameter range. Defaults to zero,
            in which case the only parameter value stored is recovery_rate
        step_size: float
            Defines the resolution of the desired parameter range, i.e. how much
            the parameter value changes as it traverses the range. Defaults to 
            zero, in which case the only parameter value stored is recovery_rate
        '''

        self.recovery_rate = self.get_range(recovery_rate, max, step_size)

    def set_fractional_timestep_size(self, fractional_timestep_size: float) -> None:
        '''Changes the model parameter fractional_timestep_size from its default.
        This model parameter is not rangeable.

        fractional_timestep_size: float
            A value between 0 and 1 that allows the simulation to be run in many
            substeps to improve accuracy. The value is the size of the timestep, 
            so a value of 0.1 means that the timestep will be run in 10 substeps 
            of size 0.1
        '''

        self.fractional_timestep_size = fractional_timestep_size

    @staticmethod
    def get_range(min, max, step_size) -> list:
        '''Takes information about the characteristics of a desired parameter
        range and returns a list of all values spanning that range. If no range 
        is desired (max or step_size is zero) then the list just contains a 
        single value.

        min
            Could be an int or a float, depending on the model parameter. If a 
            range of parameter values is desired, this is the minimum value in 
            the range. If a single parameter value is desired, this is that
            value.
        max
            Could be an int or a float, depending on the model parameter. If a 
            range of parameter values is desired, this is the maximum value in 
            the range.
        step_size
            Could be an int or a float, depending on the model parameter. If a
            range of parameter values is desired, this is the resolution of that
            range. Ex: If I want host_birth_rate to vary across a range from
            0.01 to 0.10, I can specify a step_size of 0.01 to test the values
            0.01, 0.02, 0.03 .... 0.10.

        Returns list
            A list of parameter values spanning the desired range. If a single 
            parameter value is desired, this list will only have one value.
        '''
        
        if max == 0 or step_size == 0:
            return [min]
        n_steps = round((max - min) / step_size) + 1
        return list(np.linspace(min, max, n_steps))

