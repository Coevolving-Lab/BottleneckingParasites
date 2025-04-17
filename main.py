'''This module is where you can set the simulation parameters and run the
simulation. Unless you want to dig into the model and change or add
functionality, main.py is the only script you'll need to edit and run.

In the main() function below, you'll need to create an instance of the 
Parameters class from either det_params (if running the deterministic model) or
stoch_params (if running the stochastic model).
        Ex: p1 = det_params.Parameters()

This instance will be pre-initialized with default values for all the model 
parameters (Check deterministic_parameters.py and stochastic_parameters.py to 
read more about these parameters and their default values).

To run the simulation, add det_model.run(p1) (if running the deterministic model)
or stoch_model.run(p1) (if running the stochastic model) to main(). Then run this
python script.

To alter the parameters from their default values, call any number of the setter
methods from deterministic_parameters.py / stochastic_parameters.py. Do this 
between the creation of the instance and the run statement.
    Ex:
        p1 = det_params.Parameters()
        p1.set_file_name("example")
        p1.set_n_bottlenecks(100)
        p1.set_host_birth_rate(0.01)
        p1.set_host_birth_type("Exponential")
        p1.set_transmission_rate(0.0001, 0.0005, 0.0001)
        det_model.run(p1)

The main() function contains all the code required to recreate the datasets used
in Bubrig and Gibson 2025. Each run command is commented out (with #) to prevent 
the program from trying to run them all at the same time. Remove the # character
from any run statement to get the program to run that parameter set.
'''

import deterministiccode.deterministic_parameters as det_params
import deterministiccode.deterministic_model as det_model
import stochasticcode.stochastic_parameters as stoch_params
import stochasticcode.stochastic_model as stoch_model
import os

#os.chdir([File path of Project folder here])

def main():
    ###Figure 1 - Recurring bottlenecks with three values for bottleneck frequency
    #Dataset 1: Maximum initial prevalence (black line)
    p1 = det_params.Parameters()
    p1.set_file_name("figure_1_max_prev_data")
    p1.set_n_bottlenecks(15)
    p1.set_time_till_bottleneck_mean(200, 400, 100)
    #det_model.run(p1)

    #Dataset 2: Range of initial prevalence (grey lines)
    p2 = det_params.Parameters()
    p2.set_file_name("figure_1_prev_range_data")
    p2.set_initial_popsize(100)
    p2.set_initial_prevalence(0.1, 1.0, 0.1)
    p2.set_n_bottlenecks(15)
    p2.set_time_till_bottleneck_mean(200, 400, 100)
    #det_model.run(p2)


    ###Figure 2 - pmax and pmin across range of bottleneck frequency
    p3 = det_params.Parameters()
    p3.set_file_name("figure_2_data")
    p3.set_n_bottlenecks(101)
    p3.set_burn_in(100)
    p3.set_time_till_bottleneck_mean(100, 600, 5)
    #det_model.run(p3)


    ###Figure 3 - Examples of parasite extinction
    #Dataset 1: Deterministic baseline
    p4 = det_params.Parameters()
    p4.set_file_name("figure_3_deterministic_data")
    p4.set_n_bottlenecks(100)
    p4.set_time_till_bottleneck_mean(200, 400, 100)
    #det_model.run(p4)

    #Dataset 2: Stochastic replicates
    p5 = stoch_params.Parameters()
    p5.set_file_name("figure_3_stochastic_data")
    p5.set_n_reps(20)
    p5.set_n_bottlenecks(100)
    p5.set_time_till_bottleneck_mean(200, 400, 100)
    #stoch_model.run(p5)


    ###Figure 4 - Extinction versus variation in bottleneck frequency
    #Warning: this dataset is large and takes a long time to run. Below this 
    #full-sized dataset (p6) is a low-res version (p7) for testing purposes
    p6 = stoch_params.Parameters()
    p6.set_file_name("figure_4_data")
    p6.set_n_reps(100)
    p6.set_n_bottlenecks(100)
    p6.set_burn_in(99)
    p6.set_time_till_bottleneck_mean(10, 610, 10)
    p6.set_time_till_bottleneck_cv(0, 1.0, 0.25)
    p6.set_fractional_timestep_size(1.0)
    #stoch_model.run(p6)

    #Low-res version
    p7 = stoch_params.Parameters()
    p7.set_file_name("figure_4_low_res_data")
    p7.set_n_reps(10)
    p7.set_n_bottlenecks(100)
    p7.set_burn_in(99)
    p7.set_time_till_bottleneck_mean(10, 610, 100)
    p7.set_time_till_bottleneck_cv(0, 1.0, 0.5)
    p7.set_fractional_timestep_size(1.0)
    #stoch_model.run(p7)

    

    ###Figure 5 - Extinction versus variation in bottleneck severity
    #Warning: this dataset is large and takes a long time to run. Below this 
    #full-sized dataset (p8) is a low-res version (p9) for testing purposes
    p8 = stoch_params.Parameters()
    p8.set_file_name("figure_5_data")
    p8.set_n_reps(100)
    p8.set_n_bottlenecks(100)
    p8.set_burn_in(99)
    p8.set_time_till_bottleneck_mean(300)
    p8.set_bottleneck_size_mean(10, 510, 10)
    p8.set_bottleneck_size_cv(0, 1.0, 0.25)
    p8.set_fractional_timestep_size(1.0)
    #stoch_model.run(p8)

    #Low-res version
    p9 = stoch_params.Parameters()
    p9.set_file_name("figure_5_low_res_data")
    p9.set_n_reps(10)
    p9.set_n_bottlenecks(100)
    p9.set_burn_in(99)
    p9.set_time_till_bottleneck_mean(10, 610, 100)
    p9.set_time_till_bottleneck_cv(0, 1.0, 0.5)
    p9.set_fractional_timestep_size(1.0)
    #stoch_model.run(p9)


    ####Figure S1 - Examples of population size dynamics
    p10 = det_params.Parameters()
    p10.set_file_name("figure_s1_data")
    p10.set_n_bottlenecks(6)
    p10.set_time_till_bottleneck_mean(200, 400, 200)
    p10.set_bottleneck_size_mean(250, 500, 250)
    #det_model.run(p10)


    ###Figure S2 - Examples of models with different birth and transmission functions
    #Dataset 1: Regulated birth, density-dependent transmission
    p11 = det_params.Parameters()
    p11.set_file_name("figure_s2_regulated_ddt_data")
    p11.set_n_bottlenecks(2)
    p11.set_time_till_bottleneck_mean(600)
    #det_model.run(p11)

    #Dataset 2: Exponential birth, density-dependent transmission
    p12 = det_params.Parameters()
    p12.set_file_name("figure_s2_exponential_ddt_data")
    p12.set_n_bottlenecks(2)
    p12.set_time_till_bottleneck_mean(600)
    p12.set_birth_function("Exponential")
    p12.set_fractional_timestep_size(0.0001)
    #det_model.run(p12)

    #Dataset 3: Regulated birth, frequency-dependent transmission
    p13 = det_params.Parameters()
    p13.set_file_name("figure_s2_regulated_fdt_data")
    p13.set_n_bottlenecks(2)
    p13.set_time_till_bottleneck_mean(600)
    p13.set_transmission_function("Frequency")
    p13.set_transmission_rate(0.01)
    #det_model.run(p13)

    #Dataset 4: Exponential birth, frequency-dependent transmission
    p14 = det_params.Parameters()
    p14.set_file_name("figure_s2_exponential_fdt_data")
    p14.set_n_bottlenecks(2)
    p14.set_time_till_bottleneck_mean(600)
    p14.set_birth_function("Exponential")
    p14.set_transmission_function("Frequency")
    p14.set_transmission_rate(0.05)
    #det_model.run(p14)


    ###Figure S3 - Recovery rate range
    #Dataset 1: Single bottleneck
    p15 = det_params.Parameters()
    p15.set_file_name("figure_s3_single_bottleneck_data")
    p15.set_initial_popsize(100)
    p15.set_n_bottlenecks(1)
    p15.set_time_till_bottleneck_mean(2000)
    p15.set_recovery_rate(0.0, 0.01, 0.001)
    #det_model.run(p15)

    #Dataset 2: Recurring bottlenecks
    p16 = det_params.Parameters()
    p16.set_file_name("figure_s3_recurring_bottleneck_data")
    p16.set_initial_popsize(100)
    p16.set_n_bottlenecks(15)
    p16.set_time_till_bottleneck_mean(300)
    p16.set_recovery_rate(0.0, 0.01, 0.001)
    #det_model.run(p16)


    ###Figure S4 - Infected death rate range
    #Dataset 1: Single bottleneck
    p17 = det_params.Parameters()
    p17.set_file_name("figure_s4_single_bottleneck_data")
    p17.set_initial_popsize(100)
    p17.set_n_bottlenecks(1)
    p17.set_time_till_bottleneck_mean(2000)
    p17.set_i_death_rate(0.0, 0.01, 0.001)
    #det_model.run(p17)

    #Dataset 2: Recurring bottlenecks
    p18 = det_params.Parameters()
    p18.set_file_name("figure_s4_recurring_bottleneck_data")
    p18.set_initial_popsize(100)
    p18.set_n_bottlenecks(15)
    p18.set_time_till_bottleneck_mean(300)
    p18.set_i_death_rate(0, 0.01, 0.001)
    #det_model.run(p18)


    ###Figure S5 - pmax and pmin across range of bottleneck frequency, across a range of transmission rates
    p19 = det_params.Parameters()
    p19.set_file_name("figure_s5_00125_data")
    p19.set_n_bottlenecks(101)
    p19.set_burn_in(100)
    p19.set_time_till_bottleneck_mean(0, 800, 5)
    p19.set_transmission_rate(0.0000125)
    #det_model.run(p19)

    p20 = det_params.Parameters()
    p20.set_file_name("figure_s5_0025_data")
    p20.set_n_bottlenecks(101)
    p20.set_burn_in(100)
    p20.set_time_till_bottleneck_mean(0, 800, 5)
    p20.set_transmission_rate(0.000025)
    #det_model.run(p20)

    p21 = det_params.Parameters()
    p21.set_file_name("figure_s5_005_data")
    p21.set_n_bottlenecks(101)
    p21.set_burn_in(100)
    p21.set_time_till_bottleneck_mean(0, 800, 5)
    p21.set_transmission_rate(0.00005)
    #det_model.run(p21)

    p22 = det_params.Parameters()
    p22.set_file_name("figure_s5_01_data")
    p22.set_n_bottlenecks(101)
    p22.set_burn_in(100)
    p22.set_time_till_bottleneck_mean(0, 800, 5)
    p22.set_transmission_rate(0.0001)
    #det_model.run(p22)


    ###Figure S6 - Bottleneck frequency versus extinction across a range of transmission rates
    #Warning: these datasets are very large and take a long time to run. Below
    #these 4 full-sized datasets (p23-p26) is a series of 4 low-res versions
    #(p27-p30) for testing purposes

    p23 = stoch_params.Parameters()
    p23.set_file_name("figure_s6_00125_data")
    p23.set_n_reps(100)
    p23.set_n_bottlenecks(100)
    p23.set_burn_in(99)
    p23.set_time_till_bottleneck_mean(10, 1010, 25)
    p23.set_time_till_bottleneck_cv(0, 1.0, 0.25)
    p23.set_transmission_rate(0.0000125)
    p23.set_fractional_timestep_size(1.0)
    #stoch_model.run(p23)

    p24 = stoch_params.Parameters()
    p24.set_file_name("figure_s6_0025_data")
    p24.set_n_reps(100)
    p24.set_n_bottlenecks(100)
    p24.set_burn_in(99)
    p24.set_time_till_bottleneck_mean(10, 1010, 25)
    p24.set_time_till_bottleneck_cv(0, 1.0, 0.25)
    p24.set_transmission_rate(0.000025)
    p24.set_fractional_timestep_size(1.0)
    #stoch_model.run(p24)

    p25 = stoch_params.Parameters()
    p25.set_file_name("figure_s6_005_data")
    p25.set_n_reps(100)
    p25.set_n_bottlenecks(100)
    p25.set_burn_in(99)
    p25.set_time_till_bottleneck_mean(10, 1010, 25)
    p25.set_time_till_bottleneck_cv(0, 1.0, 0.25)
    p25.set_transmission_rate(0.00005)
    p25.set_fractional_timestep_size(1.0)
    #stoch_model.run(p25)

    p26 = stoch_params.Parameters()
    p26.set_file_name("figure_s6_01_data")
    p26.set_n_reps(100)
    p26.set_n_bottlenecks(100)
    p26.set_burn_in(99)
    p26.set_time_till_bottleneck_mean(10, 1010, 25)
    p26.set_time_till_bottleneck_cv(0, 1.0, 0.25)
    p26.set_transmission_rate(0.0001)
    p26.set_fractional_timestep_size(1.0)
    #stoch_model.run(p26)

    #(Low res versions)
    p27 = stoch_params.Parameters()
    p27.set_file_name("figure_s6_low_res_00125_data")
    p27.set_n_reps(10)
    p27.set_n_bottlenecks(100)
    p27.set_burn_in(99)
    p27.set_time_till_bottleneck_mean(100, 1000, 100)
    p27.set_time_till_bottleneck_cv(0, 1.0, 0.5)
    p27.set_transmission_rate(0.0000125)
    p27.set_fractional_timestep_size(1.0)
    #stoch_model.run(p27)

    p28 = stoch_params.Parameters()
    p28.set_file_name("figure_s6_low_res_0025_data")
    p28.set_n_reps(10)
    p28.set_n_bottlenecks(100)
    p28.set_burn_in(99)
    p28.set_time_till_bottleneck_mean(100, 1000, 100)
    p28.set_time_till_bottleneck_cv(0, 1.0, 0.5)
    p28.set_transmission_rate(0.000025)
    p28.set_fractional_timestep_size(1.0)
    #stoch_model.run(p28)

    p29 = stoch_params.Parameters()
    p29.set_file_name("figure_s6_low_res_005_data")
    p29.set_n_reps(10)
    p29.set_n_bottlenecks(100)
    p29.set_burn_in(99)
    p29.set_time_till_bottleneck_mean(100, 1000, 100)
    p29.set_time_till_bottleneck_cv(0, 1.0, 0.5)
    p29.set_transmission_rate(0.00005)
    p29.set_fractional_timestep_size(1.0)
    #stoch_model.run(p29)

    p30 = stoch_params.Parameters()
    p30.set_file_name("figure_s6_low_res_01_data")
    p30.set_n_reps(10)
    p30.set_n_bottlenecks(100)
    p30.set_burn_in(99)
    p30.set_time_till_bottleneck_mean(100, 1000, 100)
    p30.set_time_till_bottleneck_cv(0, 1.0, 0.5)
    p30.set_transmission_rate(0.0001)
    p30.set_fractional_timestep_size(1.0)
    #stoch_model.run(p30)


    ###Figure S7 - pmax and pmin across range of bottleneck severity and transmission rates
    p31 = det_params.Parameters()
    p31.set_file_name("figure_s7_00125_data")
    p31.set_n_bottlenecks(101)
    p31.set_burn_in(100)
    p31.set_time_till_bottleneck_mean(300)
    p31.set_bottleneck_size_mean(10, 500, 10)
    p31.set_transmission_rate(0.0000125)
    #det_model.run(p31)

    p32 = det_params.Parameters()
    p32.set_file_name("figure_s7_0025_data")
    p32.set_n_bottlenecks(101)
    p32.set_burn_in(100)
    p32.set_time_till_bottleneck_mean(300)
    p32.set_bottleneck_size_mean(10, 500, 10)
    p32.set_transmission_rate(0.000025)
    #det_model.run(p32)

    p33 = det_params.Parameters()
    p33.set_file_name("figure_s7_005_data")
    p33.set_n_bottlenecks(101)
    p33.set_burn_in(100)
    p33.set_time_till_bottleneck_mean(300)
    p33.set_bottleneck_size_mean(10, 500, 10)
    p33.set_transmission_rate(0.00005)
    #det_model.run(p33)

    p34 = det_params.Parameters()
    p34.set_file_name("figure_s7_01_data")
    p34.set_n_bottlenecks(101)
    p34.set_burn_in(100)
    p34.set_time_till_bottleneck_mean(300)
    p34.set_bottleneck_size_mean(10, 500, 10)
    p34.set_transmission_rate(0.0001)
    #det_model.run(p34)


    ###Figure S8 - Bottleneck severity versus extinction across a range of transmission rates
    #Warning: these datasets are very large and take a long time to run. Below
    #these 4 full-sized datasets (p35-p38) is a series of 4 low-res versions
    #(p39-p42) for testing purposes

    p35 = stoch_params.Parameters()
    p35.set_file_name("figure_s8_00125_data")
    p35.set_n_reps(100)
    p35.set_n_bottlenecks(100)
    p35.set_burn_in(99)
    p35.set_time_till_bottleneck_mean(300)
    p35.set_bottleneck_size_mean(10, 1010, 25)
    p35.set_bottleneck_size_cv(0, 1.0, 0.25)
    p35.set_transmission_rate(0.0000125)
    p35.set_fractional_timestep_size(1.0)
    #stoch_model.run(p35)

    p36 = stoch_params.Parameters()
    p36.set_file_name("figure_s8_0025_data")
    p36.set_n_reps(100)
    p36.set_n_bottlenecks(100)
    p36.set_burn_in(99)
    p36.set_time_till_bottleneck_mean(300)
    p36.set_bottleneck_size_mean(10, 1010, 25)
    p36.set_bottleneck_size_cv(0, 1.0, 0.25)
    p36.set_transmission_rate(0.000025)
    p36.set_fractional_timestep_size(1.0)
    #stoch_model.run(p36)

    p37 = stoch_params.Parameters()
    p37.set_file_name("figure_s8_005_data")
    p37.set_n_reps(100)
    p37.set_n_bottlenecks(100)
    p37.set_burn_in(99)
    p37.set_time_till_bottleneck_mean(300)
    p37.set_bottleneck_size_mean(10, 1010, 25)
    p37.set_bottleneck_size_cv(0, 1.0, 0.25)
    p37.set_transmission_rate(0.00005)
    p37.set_fractional_timestep_size(1.0)
    #stoch_model.run(p37)

    p38 = stoch_params.Parameters()
    p38.set_file_name("figure_s8_01_data")
    p38.set_n_reps(100)
    p38.set_n_bottlenecks(100)
    p38.set_burn_in(99)
    p38.set_time_till_bottleneck_mean(300)
    p38.set_bottleneck_size_mean(10, 1010, 25)
    p38.set_bottleneck_size_cv(0, 1.0, 0.25)
    p38.set_transmission_rate(0.0001)
    p38.set_fractional_timestep_size(1.0)
    #stoch_model.run(p38)

    #Low-res versions
    p39 = stoch_params.Parameters()
    p39.set_file_name("figure_s8_low_res_00125_data")
    p39.set_n_reps(10)
    p39.set_n_bottlenecks(100)
    p39.set_burn_in(99)
    p39.set_time_till_bottleneck_mean(300)
    p39.set_bottleneck_size_mean(10, 1010, 100)
    p39.set_bottleneck_size_cv(0, 1.0, 0.5)
    p39.set_transmission_rate(0.0000125)
    p39.set_fractional_timestep_size(1.0)
    #stoch_model.run(p39)

    p40 = stoch_params.Parameters()
    p40.set_file_name("figure_s8_low_res_0025_data")
    p40.set_n_reps(10)
    p40.set_n_bottlenecks(100)
    p40.set_burn_in(99)
    p40.set_time_till_bottleneck_mean(300)
    p40.set_bottleneck_size_mean(10, 1010, 100)
    p40.set_bottleneck_size_cv(0, 1.0, 0.5)
    p40.set_transmission_rate(0.000025)
    p40.set_fractional_timestep_size(1.0)
    #stoch_model.run(p40)

    p41 = stoch_params.Parameters()
    p41.set_file_name("figure_s8_low_res_005_data")
    p41.set_n_reps(10)
    p41.set_n_bottlenecks(100)
    p41.set_burn_in(99)
    p41.set_time_till_bottleneck_mean(300)
    p41.set_bottleneck_size_mean(10, 1010, 100)
    p41.set_bottleneck_size_cv(0, 1.0, 0.5)
    p41.set_transmission_rate(0.00005)
    p41.set_fractional_timestep_size(1.0)
    #stoch_model.run(p41)

    p42 = stoch_params.Parameters()
    p42.set_file_name("figure_s8_low_res_01_data")
    p42.set_n_reps(10)
    p42.set_n_bottlenecks(100)
    p42.set_burn_in(99)
    p42.set_time_till_bottleneck_mean(300)
    p42.set_bottleneck_size_mean(10, 1010, 100)
    p42.set_bottleneck_size_cv(0, 1.0, 0.5)
    p42.set_transmission_rate(0.0001)
    p42.set_fractional_timestep_size(1.0)
    #stoch_model.run(p42)


    

if __name__ == "__main__":
    main()