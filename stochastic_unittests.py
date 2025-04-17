import unittest
import math

import stochasticcode.stochastic_parameters as p
import stochasticcode.stochastic_model as m
import stochasticcode.logger as l

####Testing parameters.py
class TestSetFileName(unittest.TestCase):
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(p1.file_name, "data")

    def test_set(self):
        value = "test_file_name_1"
        p1 = p.Parameters()
        p1.set_file_name(value)
        self.assertEqual(p1.file_name, value)

class TestSetNReps(unittest.TestCase):
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(p1.n_reps, 1)

    def test_set(self):
        value = 10
        p1 = p.Parameters()
        p1.set_n_reps(value)
        self.assertEqual(p1.n_reps, value)

class TestSetInitialPopsize(unittest.TestCase):
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(p1.initial_popsize, 1000)
        
    def test_set(self):
        value = 150
        p1 = p.Parameters()
        p1.set_initial_popsize(value)
        self.assertEqual(p1.initial_popsize, value)

class TestSetInitialPrevalence(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.initial_prevalence), 1)
        self.assertEqual(p1.initial_prevalence[0], 1.0)

    def test_single_value(self):
        value = 0.25
        p1 = p.Parameters()
        p1.set_initial_prevalence(value)
        self.assertEqual(len(p1.initial_prevalence), 1)
        self.assertEqual(p1.initial_prevalence[0], value)
    
    def test_range(self):
        value = 0
        max = 1.0
        step_size = 0.25

        p1 = p.Parameters()
        p1.set_initial_prevalence(value, max, step_size)
        self.assertEqual(len(p1.initial_prevalence), 5)
        self.assertAlmostEqual(p1.initial_prevalence[0], 0)
        self.assertAlmostEqual(p1.initial_prevalence[1], 0.25)
        self.assertAlmostEqual(p1.initial_prevalence[2], 0.50)
        self.assertAlmostEqual(p1.initial_prevalence[3], 0.75)
        self.assertAlmostEqual(p1.initial_prevalence[4], 1)

class TestSetNBottlenecks(unittest.TestCase):
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(p1.n_bottlenecks, 20)
        
    def test_set(self):
        value = 100
        p1 = p.Parameters()
        p1.set_n_bottlenecks(value)
        self.assertEqual(p1.n_bottlenecks, value)

class TestSetBurnIn(unittest.TestCase):
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(p1.burn_in, 0)
        
    def test_set(self):
        value = 100
        p1 = p.Parameters()
        p1.set_burn_in(value)
        self.assertEqual(p1.burn_in, value)

class TestSetBottleneckSizeMean(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.bottleneck_size_mean), 1)
        self.assertEqual(p1.bottleneck_size_mean[0], 100)

    def test_single_value(self):
        value = 20
        p1 = p.Parameters()
        p1.set_bottleneck_size_mean(value)
        self.assertEqual(len(p1.bottleneck_size_mean), 1)
        self.assertEqual(p1.bottleneck_size_mean[0], value)
    
    def test_range(self):
        value = 20
        max = 100
        step_size = 20

        p1 = p.Parameters()
        p1.set_bottleneck_size_mean(value, max, step_size)
        self.assertEqual(len(p1.bottleneck_size_mean), 5)
        self.assertEqual(p1.bottleneck_size_mean[0], 20)
        self.assertEqual(p1.bottleneck_size_mean[1], 40)
        self.assertEqual(p1.bottleneck_size_mean[2], 60)
        self.assertEqual(p1.bottleneck_size_mean[3], 80)
        self.assertEqual(p1.bottleneck_size_mean[4], 100)

class TestSetBottleneckSizeCV(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.bottleneck_size_cv), 1)
        self.assertEqual(p1.bottleneck_size_cv[0], 0)

    def test_single_value(self):
        value = 0.5
        p1 = p.Parameters()
        p1.set_bottleneck_size_cv(value)
        self.assertEqual(len(p1.bottleneck_size_cv), 1)
        self.assertEqual(p1.bottleneck_size_cv[0], value)
    
    def test_range(self):
        value = 0
        max = 1
        step_size = 0.25

        p1 = p.Parameters()
        p1.set_bottleneck_size_cv(value, max, step_size)
        self.assertEqual(len(p1.bottleneck_size_cv), 5)
        self.assertEqual(p1.bottleneck_size_cv[0], 0)
        self.assertEqual(p1.bottleneck_size_cv[1], 0.25)
        self.assertEqual(p1.bottleneck_size_cv[2], 0.5)
        self.assertEqual(p1.bottleneck_size_cv[3], 0.75)
        self.assertEqual(p1.bottleneck_size_cv[4], 1)

class TestSetTimeTillBottleneckMean(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.time_till_bottleneck_mean), 1)
        self.assertEqual(p1.time_till_bottleneck_mean[0], 75)

    def test_single_value(self):
        value = 60
        p1 = p.Parameters()
        p1.set_time_till_bottleneck_mean(value)
        self.assertEqual(len(p1.time_till_bottleneck_mean), 1)
        self.assertEqual(p1.time_till_bottleneck_mean[0], value)
    
    def test_range(self):
        value = 50
        max = 100
        step_size = 10

        p1 = p.Parameters()
        p1.set_time_till_bottleneck_mean(value, max, step_size)
        self.assertEqual(len(p1.time_till_bottleneck_mean), 6)
        self.assertEqual(p1.time_till_bottleneck_mean[0], 50)
        self.assertEqual(p1.time_till_bottleneck_mean[1], 60)
        self.assertEqual(p1.time_till_bottleneck_mean[2], 70)
        self.assertEqual(p1.time_till_bottleneck_mean[3], 80)
        self.assertEqual(p1.time_till_bottleneck_mean[4], 90)
        self.assertEqual(p1.time_till_bottleneck_mean[5], 100)

class TestSetTimeTillBottleneckCV(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.time_till_bottleneck_cv), 1)
        self.assertEqual(p1.time_till_bottleneck_cv[0], 0)

    def test_single_value(self):
        value = 0.5
        p1 = p.Parameters()
        p1.set_time_till_bottleneck_cv(value)
        self.assertEqual(len(p1.time_till_bottleneck_cv), 1)
        self.assertEqual(p1.time_till_bottleneck_cv[0], value)
    
    def test_range(self):
        value = 0
        max = 1
        step_size = 0.25

        p1 = p.Parameters()
        p1.set_time_till_bottleneck_cv(value, max, step_size)
        self.assertEqual(len(p1.time_till_bottleneck_cv), 5)
        self.assertEqual(p1.time_till_bottleneck_cv[0], 0)
        self.assertEqual(p1.time_till_bottleneck_cv[1], 0.25)
        self.assertEqual(p1.time_till_bottleneck_cv[2], 0.5)
        self.assertEqual(p1.time_till_bottleneck_cv[3], 0.75)
        self.assertEqual(p1.time_till_bottleneck_cv[4], 1)

class TestSetBirthRate(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.host_birth_rate), 1)
        self.assertEqual(p1.host_birth_rate[0], 0.03)

    def test_single_value(self):
        value = 0.01
        p1 = p.Parameters()
        p1.set_host_birth_rate(value)
        self.assertEqual(len(p1.host_birth_rate), 1)
        self.assertEqual(p1.host_birth_rate[0], value)
    
    def test_range(self):
        value = 0.01
        max = 0.05
        step_size = 0.01

        p1 = p.Parameters()
        p1.set_host_birth_rate(value, max, step_size)
        self.assertEqual(len(p1.host_birth_rate), 5)
        self.assertAlmostEqual(p1.host_birth_rate[0], 0.01)
        self.assertAlmostEqual(p1.host_birth_rate[1], 0.02)
        self.assertAlmostEqual(p1.host_birth_rate[2], 0.03)
        self.assertAlmostEqual(p1.host_birth_rate[3], 0.04)
        self.assertAlmostEqual(p1.host_birth_rate[4], 0.05)

class TestSetCarryingCapacity(unittest.TestCase):
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(p1.carrying_capacity, 1000)
        
    def test_set(self):
        value = 500
        p1 = p.Parameters()
        p1.set_carrying_capacity(value)
        self.assertEqual(p1.carrying_capacity, value)

class TestSetBirthFunction(unittest.TestCase):
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(p1.birth_type, "Regulated")
        self.assertIs(p1.birth_function, m.get_regulated_births)

    def test_set(self):
        birth_type1 = "Exponential"

        p1 = p.Parameters()
        p1.set_birth_function(birth_type1)
        self.assertEqual(p1.birth_type, birth_type1)
        self.assertIs(p1.birth_function, m.get_exponential_births)

        birth_type2 = "Regulated"
        p1.set_birth_function(birth_type2)
        self.assertEqual(p1.birth_type, birth_type2)
        self.assertIs(p1.birth_function, m.get_regulated_births)

    def test_for_error(self):
        birth_type = "Incorrect String"

        p1 = p.Parameters()
        self.assertRaises(ValueError, 
                          p1.set_birth_function, 
                          birth_type)
        
class TestSetParasiteFecundityEffect(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.parasite_fecundity_effect), 1)
        self.assertEqual(p1.parasite_fecundity_effect[0], 0)

    def test_single_value(self):
        value = 0.5
        p1 = p.Parameters()
        p1.set_parasite_fecundity_effect(value)
        self.assertEqual(len(p1.parasite_fecundity_effect), 1)
        self.assertEqual(p1.parasite_fecundity_effect[0], value)
    
    def test_range(self):
        value = 0.0
        max = 1.0
        step_size = 0.25

        p1 = p.Parameters()
        p1.set_parasite_fecundity_effect(value, max, step_size)
        self.assertEqual(len(p1.parasite_fecundity_effect), 5)
        self.assertAlmostEqual(p1.parasite_fecundity_effect[0], 0.0)
        self.assertAlmostEqual(p1.parasite_fecundity_effect[1], 0.25)
        self.assertAlmostEqual(p1.parasite_fecundity_effect[2], 0.50)
        self.assertAlmostEqual(p1.parasite_fecundity_effect[3], 0.75)
        self.assertAlmostEqual(p1.parasite_fecundity_effect[4], 1.00)

class TestSetSDeathRate(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.s_death_rate), 1)
        self.assertEqual(p1.s_death_rate[0], 0)

    def test_single_value(self):
        value = 0.01
        p1 = p.Parameters()
        p1.set_s_death_rate(value)
        self.assertEqual(len(p1.s_death_rate), 1)
        self.assertEqual(p1.s_death_rate[0], value)
    
    def test_range(self):
        value = 0.01
        max = 0.05
        step_size = 0.01

        p1 = p.Parameters()
        p1.set_s_death_rate(value, max, step_size)
        self.assertEqual(len(p1.s_death_rate), 5)
        self.assertAlmostEqual(p1.s_death_rate[0], 0.01)
        self.assertAlmostEqual(p1.s_death_rate[1], 0.02)
        self.assertAlmostEqual(p1.s_death_rate[2], 0.03)
        self.assertAlmostEqual(p1.s_death_rate[3], 0.04)
        self.assertAlmostEqual(p1.s_death_rate[4], 0.05)

class TestSetIDeathRate(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.i_death_rate), 1)
        self.assertEqual(p1.i_death_rate[0], 0)

    def test_single_value(self):
        value = 0.01
        p1 = p.Parameters()
        p1.set_i_death_rate(value)
        self.assertEqual(len(p1.i_death_rate), 1)
        self.assertEqual(p1.i_death_rate[0], value)
    
    def test_range(self):
        value = 0.01
        max = 0.05
        step_size = 0.01

        p1 = p.Parameters()
        p1.set_i_death_rate(value, max, step_size)
        self.assertEqual(len(p1.i_death_rate), 5)
        self.assertAlmostEqual(p1.i_death_rate[0], 0.01)
        self.assertAlmostEqual(p1.i_death_rate[1], 0.02)
        self.assertAlmostEqual(p1.i_death_rate[2], 0.03)
        self.assertAlmostEqual(p1.i_death_rate[3], 0.04)
        self.assertAlmostEqual(p1.i_death_rate[4], 0.05)

class TestSetRDeathRate(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.r_death_rate), 1)
        self.assertEqual(p1.r_death_rate[0], 0)

    def test_single_value(self):
        value = 0.01
        p1 = p.Parameters()
        p1.set_r_death_rate(value)
        self.assertEqual(len(p1.r_death_rate), 1)
        self.assertEqual(p1.r_death_rate[0], value)
    
    def test_range(self):
        value = 0.01
        max = 0.05
        step_size = 0.01

        p1 = p.Parameters()
        p1.set_r_death_rate(value, max, step_size)
        self.assertEqual(len(p1.r_death_rate), 5)
        self.assertAlmostEqual(p1.r_death_rate[0], 0.01)
        self.assertAlmostEqual(p1.r_death_rate[1], 0.02)
        self.assertAlmostEqual(p1.r_death_rate[2], 0.03)
        self.assertAlmostEqual(p1.r_death_rate[3], 0.04)
        self.assertAlmostEqual(p1.r_death_rate[4], 0.05)

class TestSetTransmissionRate(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(len(p1.transmission_rate), 1)
        self.assertEqual(p1.transmission_rate[0], 0.0001)

    def test_single_value(self):
        value = 0.00015
        p1 = p.Parameters()
        p1.set_transmission_rate(value)
        self.assertEqual(len(p1.transmission_rate), 1)
        self.assertEqual(p1.transmission_rate[0], value)
    
    def test_range(self):
        value = 0.0001
        max = 0.0005
        step_size = 0.0001

        p1 = p.Parameters()
        p1.set_transmission_rate(value, max, step_size)
        self.assertEqual(len(p1.transmission_rate), 5)
        self.assertAlmostEqual(p1.transmission_rate[0], 0.0001)
        self.assertAlmostEqual(p1.transmission_rate[1], 0.0002)
        self.assertAlmostEqual(p1.transmission_rate[2], 0.0003)
        self.assertAlmostEqual(p1.transmission_rate[3], 0.0004)
        self.assertAlmostEqual(p1.transmission_rate[4], 0.0005)
    
class TestSetTransmissionFunction(unittest.TestCase):
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(p1.transmission_type, "Density")
        self.assertIs(p1.transmission_function, m.get_ddt_infections)

    def test_set(self):
        transmission_type1 = "Frequency"

        p1 = p.Parameters()
        p1.set_transmission_function(transmission_type1)
        self.assertEqual(p1.transmission_type, transmission_type1)
        self.assertIs(p1.transmission_function, m.get_fdt_infections)

        transmission_type2 = "Density"
        p1.set_transmission_function(transmission_type2)
        self.assertEqual(p1.transmission_type, transmission_type2)
        self.assertIs(p1.transmission_function, m.get_ddt_infections)

    def test_for_error(self):
        transmission_type = "Incorrect String"

        p1 = p.Parameters()
        self.assertRaises(ValueError, 
                          p1.set_transmission_function, 
                          transmission_type)
    
class TestSetRecoveryRate(unittest.TestCase):
    #Since this is a rangeable model parameter, it is stored in list form
    def test_default(self):    
        p1 = p.Parameters()
        self.assertEqual(len(p1.recovery_rate), 1)
        self.assertEqual(p1.recovery_rate[0], 0)

    def test_single_value(self):
        value = 0.05
        p1 = p.Parameters()
        p1.set_recovery_rate(value)
        self.assertEqual(len(p1.recovery_rate), 1)
        self.assertEqual(p1.recovery_rate[0], value)
    
    def test_range(self):
        value = 0.05
        max = 0.1
        step_size = 0.01

        p1 = p.Parameters()
        p1.set_recovery_rate(value, max, step_size)
        self.assertEqual(len(p1.recovery_rate), 6)
        self.assertAlmostEqual(p1.recovery_rate[0], 0.05)
        self.assertAlmostEqual(p1.recovery_rate[1], 0.06)
        self.assertAlmostEqual(p1.recovery_rate[2], 0.07)
        self.assertAlmostEqual(p1.recovery_rate[3], 0.08)
        self.assertAlmostEqual(p1.recovery_rate[4], 0.09)
        self.assertAlmostEqual(p1.recovery_rate[5], 0.1)

class TestSetFractionalTimestepSize(unittest.TestCase):
    def test_default(self):
        p1 = p.Parameters()
        self.assertEqual(p1.fractional_timestep_size, 1.0)
        
    def test_set(self):
        value = 0.1
        p1 = p.Parameters()
        p1.set_fractional_timestep_size(value)
        self.assertEqual(p1.fractional_timestep_size, value)

class TestGetRange(unittest.TestCase):
    def test_max_zero(self):
        min = 10
        max = 0
        step_size = 1

        range = p.Parameters.get_range(min, max, step_size)
        self.assertEqual(len(range), 1)
        self.assertEqual(range[0], 10)

    def test_step_size_zero(self):
        min = 10
        max = 20
        step_size = 0

        range = p.Parameters.get_range(min, max, step_size)
        self.assertEqual(len(range), 1)
        self.assertEqual(range[0], 10)

    def test_both_zero(self):
        min = 10
        max = 0
        step_size = 0

        range = p.Parameters.get_range(min, max, step_size)
        self.assertEqual(len(range), 1)
        self.assertEqual(range[0], 10)
   
    def test_range_ints(self):
        min = 10
        max = 16
        step_size = 1

        range = p.Parameters.get_range(min, max, step_size)
        self.assertEqual(len(range), 7)
        self.assertEqual(range[0], 10)
        self.assertEqual(range[1], 11)
        self.assertEqual(range[2], 12)
        self.assertEqual(range[3], 13)
        self.assertEqual(range[4], 14)
        self.assertEqual(range[5], 15)
        self.assertEqual(range[6], 16)

    def test_range_floats(self):
        min = 0.1
        max = 0.6
        step_size = 0.1

        range = p.Parameters.get_range(min, max, step_size)
        self.assertEqual(len(range), 6)
        self.assertAlmostEqual(range[0], 0.1)
        self.assertAlmostEqual(range[1], 0.2)
        self.assertAlmostEqual(range[2], 0.3)
        self.assertAlmostEqual(range[3], 0.4)
        self.assertAlmostEqual(range[4], 0.5)
        self.assertAlmostEqual(range[5], 0.6)



####Testing model.py
class TestRunModel(unittest.TestCase):
    '''The main unique things in this function are incrementing the series
    number and calling run_timepoint multiple times. I will run a model with
    a exponential birth function, compare the population size before and after
    this function is called to ensure that run_timepoint is called the correct
    number of times
    '''
    def tearDown(self):
        m.series = 1

    def test_series_increment(self):
        self.assertEqual(m.series, 1)

        dataframe = l.Dataframe(file_name = "test1")
        s, i, r = m.run_model(dataframe, current_rep = 1, is_logging=False, 
                              n_timepoints=2, fractional_timestep_size=1.0, 
                              s=10, i=0, r=0,
                              birth_function=m.get_exponential_births,
                              host_birth_rate=0, carrying_capacity=None,
                              parasite_fecundity_effect=0,
                              transmission_function=m.get_ddt_infections,
                              transmission_rate=0, s_death_rate=0, i_death_rate=0,
                              r_death_rate=0, recovery_rate=0)
        self.assertEqual(m.series, 2)

    def test_correct_n_timepoints(self):
        dataframe = l.Dataframe(file_name = "test1")
        current_rep = 1
        is_logging = False
        n_timepoints = 4
        fractional_timestep_size = 1.0
        s = 2
        i = 0
        r = 0
        birth_function = m.get_exponential_births
        host_birth_rate = 1.0
        carrying_capacity = None
        parasite_fecundity_effect = 0
        transmission_function = m.get_ddt_infections
        transmission_rate = 0
        s_death_rate = 0
        i_death_rate = 0
        r_death_rate = 0
        recovery_rate = 0

        s, i, r = m.run_model(dataframe, current_rep, is_logging, n_timepoints, 
                              fractional_timestep_size, s, i, r, birth_function, 
                              host_birth_rate, carrying_capacity, 
                              parasite_fecundity_effect, transmission_function, 
                              transmission_rate, s_death_rate, i_death_rate, 
                              r_death_rate, recovery_rate)
        
        self.assertAlmostEqual(s, 32)
        

class TestRunTimepoint(unittest.TestCase):
    '''Combines the results from several sub functions that are tested below.
    The main thing is to check that it is combining them correctly and that it
    is running fractional timesteps correctly.
    '''
    
    def test_births(self):
        fractional_timestep_size = 1.0
        s = 10
        i = 0
        r = 0
        birth_function = m.get_exponential_births
        host_birth_rate = 1.0
        carrying_capacity = None
        parasite_fecundity_effect = 0
        transmission_function = m.get_ddt_infections
        transmission_rate = 0
        s_death_rate = 0
        i_death_rate = 0
        r_death_rate = 0
        recovery_rate = 0

        s, i, r = m.run_timepoint(fractional_timestep_size, s, i, r, 
                                  birth_function, host_birth_rate, carrying_capacity,
                                  parasite_fecundity_effect, transmission_function,
                                  transmission_rate, s_death_rate, i_death_rate,
                                  r_death_rate, recovery_rate)
        self.assertEqual(s, 20)
        self.assertEqual(i, 0)
        self.assertEqual(r, 0)


class TestGetTimeTillBottleneck(unittest.TestCase):
    def test_no_variance(self):
        time_till_bottleneck_mean = 100
        time_till_bottleneck_cv = 0

        time_till_bottleneck = m.get_time_till_bottleneck(time_till_bottleneck_mean,
                                                          time_till_bottleneck_cv)
        self.assertEqual(time_till_bottleneck, 100)

    def test_variance_no_zeros(self):
        time_till_bottleneck_mean = 10
        time_till_bottleneck_cv = 0.1

        for _ in range(1000):
            time_till_bottleneck = m.get_time_till_bottleneck(time_till_bottleneck_mean,
                                                              time_till_bottleneck_cv)
            self.assertGreater(time_till_bottleneck, 0)
    
    def test_mean(self):
        time_till_bottleneck_mean = 100
        time_till_bottleneck_cv = 0.01
        n_reps = 10000
        running_total = 0
        tolerance = 1

        for _ in range(n_reps):
            running_total += m.get_time_till_bottleneck(time_till_bottleneck_mean,
                                                        time_till_bottleneck_cv)
        
        mean = running_total / n_reps
        self.assertGreaterEqual(mean, time_till_bottleneck_mean - tolerance)
        self.assertLessEqual(mean, time_till_bottleneck_mean + tolerance)


class TestGetBottleneckSize(unittest.TestCase):
    def test_no_variance(self):
        bottleneck_size_mean = 100
        bottleneck_size_cv = 0

        bottleneck_size = m.get_bottleneck_size(bottleneck_size_mean,
                                                bottleneck_size_cv)
        self.assertEqual(bottleneck_size, 100)

    def test_variance_no_zeros(self):
        bottleneck_size_mean = 10
        bottleneck_size_cv = 0.1

        for _ in range(1000):
            bottleneck_size = m.get_bottleneck_size(bottleneck_size_mean,
                                                    bottleneck_size_cv)
            self.assertGreater(bottleneck_size, 0)

    def test_mean(self):
        bottleneck_size_mean = 100
        bottleneck_size_cv = 0.01
        n_reps = 1000
        running_total = 0
        tolerance = 1

        for _ in range(n_reps):
            running_total += m.get_bottleneck_size(bottleneck_size_mean,
                                                  bottleneck_size_cv)
            
        mean = running_total / n_reps
        self.assertGreaterEqual(mean, bottleneck_size_mean - tolerance)
        self.assertLessEqual(mean, bottleneck_size_mean + tolerance)
            
      
class TestGetBottleneckSurvivors(unittest.TestCase):
    def test_guaranteed_sampling_s(self):
        s = 1000
        i = 0
        r = 0
        bottleneck_size = 100
        n_reps = 1000

        for _ in range(n_reps):
            new_s, new_i, new_r = m.get_bottleneck_survivors(s, i, r,
                                                            bottleneck_size)
            self.assertEqual(new_s, 100)
            self.assertEqual(new_i, 0)
            self.assertEqual(new_r, 0)

    def test_guaranteed_sampling_i(self):
        s = 0
        i = 1000
        r = 0
        bottleneck_size = 100
        n_reps = 1000

        for _ in range(n_reps):
            new_s, new_i, new_r = m.get_bottleneck_survivors(s, i, r,
                                                            bottleneck_size)
            self.assertEqual(new_s, 0)
            self.assertEqual(new_i, 100)
            self.assertEqual(new_r, 0)

    def test_guaranteed_sampling_r(self):
        s = 0
        i = 0
        r = 1000
        bottleneck_size = 100
        n_reps = 1000

        for _ in range(n_reps):
            new_s, new_i, new_r = m.get_bottleneck_survivors(s, i, r,
                                                            bottleneck_size)
            self.assertEqual(new_s, 0)
            self.assertEqual(new_i, 0)
            self.assertEqual(new_r, 100)
    
    def test_combination_bottleneck(self):
        #Combo 1
        s = 500
        i = 500
        r = 0
        bottleneck_size = 100
        target_average_prevalence = i / (s + i + r)
        tolerance = 0.05
        n_reps = 1000
        running_prevalence = 0

        for _ in range(n_reps):
            
            new_s, new_i, new_r = m.get_bottleneck_survivors(s, i, r,
                                                            bottleneck_size)
            post_bottleneck_prevalence = new_i / (new_s + new_i + new_r)
            running_prevalence += post_bottleneck_prevalence
        
        average_prevalence = running_prevalence / n_reps
        self.assertGreaterEqual(average_prevalence, 
                                target_average_prevalence - tolerance)
        self.assertLessEqual(average_prevalence,
                             target_average_prevalence + tolerance)


        #Combo 2
        s = 100
        i = 900
        r = 0
        bottleneck_size = 100
        target_average_prevalence = i / (s + i + r)
        tolerance = 0.05
        n_reps = 1000
        running_prevalence = 0

        for _ in range(n_reps):
            
            new_s, new_i, new_r = m.get_bottleneck_survivors(s, i, r,
                                                            bottleneck_size)
            post_bottleneck_prevalence = new_i / (new_s + new_i + new_r)
            running_prevalence += post_bottleneck_prevalence
        
        average_prevalence = running_prevalence / n_reps
        self.assertGreaterEqual(average_prevalence, 
                                target_average_prevalence - tolerance)
        self.assertLessEqual(average_prevalence,
                             target_average_prevalence + tolerance)
        
    def test_decimal_inputs(self):
        s = 100.55
        i = 100.55
        r = 0
        bottleneck_size = 100
        target_average_prevalence = i / (s + i + r)
        tolerance = 0.05
        n_reps = 1000
        running_prevalence = 0

        for _ in range(n_reps):
            
            new_s, new_i, new_r = m.get_bottleneck_survivors(s, i, r,
                                                            bottleneck_size)
            post_bottleneck_prevalence = new_i / (new_s + new_i + new_r)
            running_prevalence += post_bottleneck_prevalence
        
        average_prevalence = running_prevalence / n_reps
        self.assertGreaterEqual(average_prevalence, 
                                target_average_prevalence - tolerance)
        self.assertLessEqual(average_prevalence,
                             target_average_prevalence + tolerance)
        
    def test_for_int_outputs(self):
        s = 100
        i = 100
        r = 0
        bottleneck_size = 100
        n_reps = 1000

        for _ in range(n_reps):
            
            new_s, new_i, new_r = m.get_bottleneck_survivors(s, i, r,
                                                            bottleneck_size)
            self.assertAlmostEqual(new_s - math.floor(new_s), 0)
            self.assertAlmostEqual(new_i - math.floor(new_i), 0)
            self.assertAlmostEqual(new_r - math.floor(new_r), 0)
            
    

class TestGetRegulatedBirths(unittest.TestCase):

    def test_no_host_birth(self):
        s = 200
        i = 200
        r = 100
        host_birth_rate = 0
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 0)
    
    def test_at_carrying_capacity(self):
        s = 500
        i = 250
        r = 250
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 0)

    def test_above_carrying_capacity(self):
        s = 501
        i = 250
        r = 250
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 0)

    def test_host_birth_from_s(self):
        s = 500
        i = 0
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 2.5)

    def test_host_birth_from_i(self):
        s = 0
        i = 500
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 2.5)

    def test_host_birth_from_r(self):
        s = 0
        i = 0
        r = 500
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 2.5)

    def test_combination(self):
        s = 100
        i = 100
        r = 300
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 2.5)

        s = 300
        i = 300
        r = 150
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 1.875)

    def test_fecundity_effect(self):
        s = 0
        i = 500
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 2.5)

        s = 0
        i = 500
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0.5
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 1.25)

        s = 0
        i = 500
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 1.0
        fractional_timestep_size = 1.0

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 0)

    def test_fractional_timestep(self):
        s = 100
        i = 100
        r = 300
        host_birth_rate = 0.01
        carrying_capacity = 1000
        parasite_fecundity_effect = 0
        fractional_timestep_size = 0.1

        new_births = m.get_regulated_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 0.25)


class TestGetExponentialBirths(unittest.TestCase):

    def test_no_host_birth(self):
        s = 100
        i = 100
        r = 100
        host_birth_rate = 0
        carrying_capacity = None
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 0)
    
    def test_host_birth_from_s(self):
        s = 100
        i = 0
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = None
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 1)

    def test_host_birth_from_i(self):
        s = 0
        i = 100
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = None
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 1)

    def test_host_birth_from_r(self):
        s = 0
        i = 0
        r = 100
        host_birth_rate = 0.01
        carrying_capacity = None
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 1)

    def test_combination(self):
        s = 100
        i = 200
        r = 300
        host_birth_rate = 0.01
        carrying_capacity = None
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 6)

        s = 200
        i = 200
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = None
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 4)

    def test_fecundity_effect(self):
        s = 0
        i = 100
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = None
        parasite_fecundity_effect = 0
        fractional_timestep_size = 1.0

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 1)

        s = 0
        i = 100
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = None
        parasite_fecundity_effect = 0.5
        fractional_timestep_size = 1.0

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 0.5)

        s = 0
        i = 100
        r = 0
        host_birth_rate = 0.01
        carrying_capacity = None
        parasite_fecundity_effect = 1.0
        fractional_timestep_size = 1.0

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertEqual(new_births, 0)

    def test_fractional_timestep(self):
        s = 100
        i = 200
        r = 300
        host_birth_rate = 0.01
        carrying_capacity = None
        parasite_fecundity_effect = 0
        fractional_timestep_size = 0.1

        new_births = m.get_exponential_births(s, i, r, host_birth_rate,
                                              carrying_capacity, 
                                              parasite_fecundity_effect,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_births, 0.6)
        

class TestGetSDeaths(unittest.TestCase):
    def test_no_susceptibles(self):
        s = 0
        s_death_rate = 0.1
        fractional_timestep_size = 1.0

        new_s_deaths = m.get_s_deaths(s, s_death_rate, fractional_timestep_size)
        self.assertEqual(new_s_deaths, 0)

    def test_no_s_death(self):
        s = 10
        s_death_rate = 0
        fractional_timestep_size = 1.0

        new_s_deaths = m.get_s_deaths(s, s_death_rate, fractional_timestep_size)
        self.assertEqual(new_s_deaths, 0)

    def test_s_death(self):
        s = 10
        s_death_rate = 0.1
        fractional_timestep_size = 1.0

        new_s_deaths = m.get_s_deaths(s, s_death_rate, fractional_timestep_size)
        self.assertEqual(new_s_deaths, 1)

        s = 150
        s_death_rate = 0.1
        fractional_timestep_size = 1.0

        new_s_deaths = m.get_s_deaths(s, s_death_rate, fractional_timestep_size)
        self.assertEqual(new_s_deaths, 15)

    def test_fractional_timestep(self):
        s = 150
        s_death_rate = 0.1
        fractional_timestep_size = 0.1

        new_s_deaths = m.get_s_deaths(s, s_death_rate, fractional_timestep_size)
        self.assertAlmostEqual(new_s_deaths, 1.5)



class TestGetIDeaths(unittest.TestCase):
    def test_no_infecteds(self):
        i = 0
        i_death_rate = 0.1
        fractional_timestep_size = 1.0

        new_i_deaths = m.get_i_deaths(i, i_death_rate, fractional_timestep_size)
        self.assertEqual(new_i_deaths, 0)

    def test_no_i_death(self):
        i = 10
        i_death_rate = 0
        fractional_timestep_size = 1.0

        new_i_deaths = m.get_i_deaths(i, i_death_rate, fractional_timestep_size)
        self.assertEqual(new_i_deaths, 0)

    def test_i_death(self):
        i = 10
        i_death_rate = 0.1
        fractional_timestep_size = 1.0

        new_i_deaths = m.get_i_deaths(i, i_death_rate, fractional_timestep_size)
        self.assertEqual(new_i_deaths, 1)

        i = 150
        i_death_rate = 0.1
        fractional_timestep_size = 1.0

        new_i_deaths = m.get_i_deaths(i, i_death_rate, fractional_timestep_size)
        self.assertEqual(new_i_deaths, 15)

    def test_fractional_timestep(self):
        i = 150
        i_death_rate = 0.1
        fractional_timestep_size = 0.1

        new_i_deaths = m.get_i_deaths(i, i_death_rate, fractional_timestep_size)
        self.assertAlmostEqual(new_i_deaths, 1.5)


class TestGetRDeaths(unittest.TestCase):
    def test_no_recovereds(self):
        r = 0
        r_death_rate = 0.1
        fractional_timestep_size = 1.0

        new_r_deaths = m.get_r_deaths(r, r_death_rate, fractional_timestep_size)
        self.assertEqual(new_r_deaths, 0)

    def test_no_r_death(self):
        r = 10
        r_death_rate = 0
        fractional_timestep_size = 1.0

        new_r_deaths = m.get_r_deaths(r, r_death_rate, fractional_timestep_size)
        self.assertEqual(new_r_deaths, 0)

    def test_r_death(self):
        r = 10
        r_death_rate = 0.1
        fractional_timestep_size = 1.0

        new_r_deaths = m.get_r_deaths(r, r_death_rate, fractional_timestep_size)
        self.assertEqual(new_r_deaths, 1)

        r = 150
        r_death_rate = 0.1
        fractional_timestep_size = 1.0

        new_r_deaths = m.get_r_deaths(r, r_death_rate, fractional_timestep_size)
        self.assertEqual(new_r_deaths, 15)

    def test_fractional_timestep(self):
        r = 150
        r_death_rate = 0.1
        fractional_timestep_size = 0.1

        new_r_deaths = m.get_r_deaths(r, r_death_rate, fractional_timestep_size)
        self.assertAlmostEqual(new_r_deaths, 1.5)


class TestGetDDTInfections(unittest.TestCase):
    def test_no_susceptibles(self):
        s = 0
        i = 100
        r = 0
        transmission_rate = 0.0001
        fractional_timestep_size = 1.0

        new_infections = m.get_ddt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertEqual(new_infections, 0)

    def test_no_infecteds(self):
        s = 100
        i = 0
        r = 0
        transmission_rate = 0.0001
        fractional_timestep_size = 1.0

        new_infections = m.get_ddt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertEqual(new_infections, 0)
    
    def test_no_transmission(self):
        s = 100
        i = 100
        r = 0
        transmission_rate = 0
        fractional_timestep_size = 1.0

        new_infections = m.get_ddt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertEqual(new_infections, 0)
    
    def test_infections(self):
        s = 100
        i = 100
        r = 0
        transmission_rate = 0.0001
        fractional_timestep_size = 1.0

        new_infections = m.get_ddt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertEqual(new_infections, 1)

        s = 200
        i = 200
        r = 0
        transmission_rate = 0.0001
        fractional_timestep_size = 1.0

        new_infections = m.get_ddt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertEqual(new_infections, 4)

    def test_fractional_timestep(self):
        s = 100
        i = 100
        r = 0
        transmission_rate = 0.0001
        fractional_timestep_size = 0.1

        new_infections = m.get_ddt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_infections, 0.1)
        

class TestGetFDTInfections(unittest.TestCase):
    def test_no_susceptibles(self):
        s = 0
        i = 100
        r = 0
        transmission_rate = 0.1
        fractional_timestep_size = 1.0

        new_infections = m.get_fdt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertEqual(new_infections, 0)

    def test_no_infecteds(self):
        s = 100
        i = 0
        r = 0
        transmission_rate = 0.1
        fractional_timestep_size = 1.0

        new_infections = m.get_fdt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertEqual(new_infections, 0)
    
    def test_no_transmission(self):
        s = 100
        i = 100
        r = 0
        transmission_rate = 0
        fractional_timestep_size = 1.0

        new_infections = m.get_fdt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertEqual(new_infections, 0)

    def test_infections(self):
        s = 100
        i = 100
        r = 0
        transmission_rate = 0.1
        fractional_timestep_size = 1.0

        new_infections = m.get_fdt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertEqual(new_infections, 5)

        s = 300
        i = 100
        r = 0
        transmission_rate = 0.1
        fractional_timestep_size = 1.0

        new_infections = m.get_fdt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_infections, 7.5)


    def test_infections_with_r(self):
        s = 100
        i = 100
        r = 200
        transmission_rate = 0.1
        fractional_timestep_size = 1.0

        new_infections = m.get_fdt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_infections, 2.5)

    def test_fractional_timestep(self):
        s = 100
        i = 100
        r = 0
        transmission_rate = 0.1
        fractional_timestep_size = 0.1

        new_infections = m.get_fdt_infections(s, i, r, transmission_rate,
                                              fractional_timestep_size)
        self.assertAlmostEqual(new_infections, 0.5)


class TestGetRecoveries(unittest.TestCase):
    def test_no_infecteds(self):
        i = 0
        recovery_rate = 0.1
        fractional_timestep_size = 1.0

        new_recoveries = m.get_recoveries(i, recovery_rate, 
                                          fractional_timestep_size)
        self.assertEqual(new_recoveries, 0)

    def test_no_recovery(self):
        i = 100
        recovery_rate = 0
        fractional_timestep_size = 1.0

        new_recoveries = m.get_recoveries(i, recovery_rate, 
                                          fractional_timestep_size)
        self.assertEqual(new_recoveries, 0)
    
    def test_get_recoveries(self):
        i = 100
        recovery_rate = 0.1
        fractional_timestep_size = 1.0

        new_recoveries = m.get_recoveries(i, recovery_rate, 
                                          fractional_timestep_size)
        self.assertEqual(new_recoveries, 10)

    def test_fractional_timestep(self):
        i = 100
        recovery_rate = 0.1
        fractional_timestep_size = 0.1

        new_recoveries = m.get_recoveries(i, recovery_rate, 
                                          fractional_timestep_size)
        self.assertEqual(new_recoveries, 1)



if __name__ == '__main__':
    unittest.main()