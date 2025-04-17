# BottleneckingParasites
This Python project and the associated outputs are part of the manuscript Bubrig and Gibson 2025 “Boom-bust cycles constrain host-parasite dynamics, suppress parasite spread, and drive parasites extinct” at The American Naturalist

Authors:
 - Louis T. Bubrig (ltb4pv@virginia.edu)
 - Amanda K. Gibson

Project summary:
This study investigated host-parasite dynamics under boom-bust conditions, i.e. when host populations experience alternating periods of dramatic population growth followed by population crashes. The study looked at a discrete time deterministic compartment (Susceptible-Infected, or SI) model. Boom-bust dynamics were simulated by subjecting the host population to recurring population bottlenecks which repeatedly crashed the population to a low density. Bottlenecks were either modeled as deterministic or stochastic. Deterministic bottlenecks were used to determine how the boom-bust dynamics influenced parasite spread, while stochastic bottlenecks were used to determine which conditions drove the parasite extinct. Recurring bottlenecks were parameterized with a frequency (which defined the number of simulation timepoints between bottlenecks) and a severity (which defined the number of hosts that survived each bottleneck).

All code was written and all data were collected and analyzed by LTB. Note that all simulations run for Bubrig and Gibson 2025 were run with parameters 1/100 the value of those reported in the paper for computational precision. All reported parameters were scaled back up by a factor of 100 in the R data wrangling and visualization process.

Summary of workflow:
In the root directory is the Python entry point “main.py”. This is the only Python file needed to run simulations and output data. Within main.py, the user can generate a parameter set for a model with either deterministic or stochastic bottlenecks. The parameter set comes pre-loaded with
default values, but the user can modify those parameter values or tell the simulation to run across a range of values for one or more parameters. Once the parameter set is acceptable, the user can then run that parameter set, which runs the simulation and outputs the data into the ./output/ folder. The actual
Python code to run the model with deterministic bottlenecks is in the ./deterministiccode/ folder, and the code to run the model with stochastic bottlenecks is in the ./stochasticcode/ folder. The main.py also contains all the parameter sets used to generate the data found in the manuscript Bubrig and Gibson 2025 (“Boom-bust cycles constrain host-parasite dynamics, suppress parasite spread, and drive parasites extinct”), so that the user can replicate those datasets.
Also in the root directory is Visualization.R, which contains all the R code needed to scoop the raw data from ./output/ , perform data wrangling and plot generation, and export the figures used in the manuscript. Those figures, along with any Powerpoint formatting files, are found in their respective
folders within ./Figures/

Finally, the root directory also contains deterministic_unittests.py and stochastic_unittests.py which test nearly all critical functions and methods found in the Python code to ensure that they work as expected.

Dependencies:
For R (version 4.4.0) 
	- ggplot2 (version 3.5.1)
	- dplyr (version 1.1.4)
	- tidyr (version 1.3.1)
For Python (version 3.10.0)
	- numpy (version 2.1.3)
		- Needed in:
			./deterministiccode/deterministic_parameters.py
			./deterministiccode/deterministic_model.py
			./stochasticcode/stochastic_parameters.py
			./stochasticcode/stochastic_model.py
	- unittest (standard library)
		- Needed in:
			./deterministic_unittests.py
			./stochastic_unittests.py
	- typing (standard library)
		- Needed in:
			./deterministiccode/deterministic_parameters.py
			./deterministiccode/deterministic_model.py
			./stochasticcode/stochastic_parameters.py
			./stochasticcode/stochastic_model.py
	- itertools (standard library)
		- Needed in:
			./deterministiccode/deterministic_model.py
			./stochasticcode/stochastic_model.py
	- csv (standard library)
		-Needed in:
			./deterministiccode/logger.py
			./stochasticcode/logger.py
			


Structure of folders and files:

.
|—README.rtf
|—Visualization.R
|—main.py
|—deterministic_unittests.py
|—stochastic_unittests.py
|—deterministiccode/
|     |—deterministic_model.py
|     |—deterministic_parameters.py
|     |—logger.py
|—stochasticcode/
|     |—stochastic_model.py
|     |—stochastic_parameters.py
|     |—logger.py
|—output/
|     |—figure_1_max_prev_data.csv
|     |—figure_1_prev_range_data.csv
|     |—figure_2_data.csv
|     |—figure_3_deterministic_data.csv
|     |—figure_3_stochastic_data.csv
|     |—figure_4_data.csv
|     |—figure_5_data.csv
|     |—figure_s1_data.csv
|     |—figure_s2_exponential_ddt_data.csv
|     |—figure_s2_exponential_fdt_data.csv
|     |—figure_s2_regulated_ddt_data.csv
|     |—figure_s2_regulated_fdt_data.csv
|     |—figure_s3_recurring_bottleneck_data.csv
|     |—figure_s3_single_bottleneck_data.csv
|     |—figure_s4_recurring_bottleneck_data.csv
|     |—figure_s4_single_bottleneck_data.csv
|     |—figure_s5_01_data.csv
|     |—figure_s5_005_data.csv
|     |—figure_s5_0025_data.csv
|     |—figure_s5_00125_data.csv
|     |—figure_s6_01_data.csv
|     |—figure_s6_005_data.csv
|     |—figure_s6_0025_data.csv
|     |—figure_s6_00125_data.csv
|     |—figure_s7_01_data.csv
|     |—figure_s7_005_data.csv
|     |—figure_s7_0025_data.csv
|     |—figure_s7_00125_data.csv
|     |—figure_s8_01_data.csv
|     |—figure_s8_005_data.csv
|     |—figure_s8_0025_data.csv
|     |—figure_s8_00125_data.csv
|—Figures/
|     |—Figure 1/
|     |     |—2 Panel.tiff
|     |     |—3 Panel.tiff
|     |     |—4 Panel.tiff
|     |     |—Empty Panels.tiff
|     |     |—Figure 1.png
|     |     |—Figure 1 Formatting.pptx
|     |—Figure 2/
|     |     |—Figure 2.png
|     |     |—Figure 2 Formatting.pptx
|     |     |—Figure 2 Unlabeled.tiff
|     |—Figure 3/
|     |     |—2 Panel.tiff
|     |     |—3 Panel.tiff
|     |     |—4 Panel.tiff
|     |     |—Empty Panels.tiff
|     |     |—Figure 3.png
|     |     |—Figure 3 Formatting.pptx
|     |—Figure 4/
|     |     |—Figure 4.tiff
|     |     |—figure_4_summarized_data.csv
|     |—Figure 5/
|     |     |—Figure 5.tiff
|     |     |—figure_5_summarized_data.csv
|     |—Figure S1/
|     |     |—Figure S1.png
|     |     |—Figure S1 Formatting.pptx
|     |     |—Figure S1 Unlabeled.tiff
|     |—Figure S2/
|     |     |—Figure S2.tiff
|     |—Figure S3/
|     |     |—Figure S3.png
|     |     |—Figure S3 Formatting.pptx
|     |     |—Figure S3 Recurring Bottleneck Panel.tiff
|     |     |—Figure S3 Single Bottleneck Panel.tiff
|     |     |—Figure S3 SIR Panel.tiff
|     |—Figure S4/
|     |     |—Figure S4.png
|     |     |—Figure S4 Formatting.pptx
|     |     |—Figure S4 Recurring Bottleneck Panel.tiff
|     |     |—Figure S4 Single Bottleneck Panel.tiff
|     |—Figure S5/
|     |     |—Figure S5.tiff
|     |—Figure S6/
|     |     |—Figure S6.png
|     |     |—Figure S6 Formatting.pptx
|     |     |—Figure S6 Unlabeled.tiff
|     |     |—figure_s6_summarized_data.csv
|     |—Figure S7/
|     |     |—Figure S7.tiff
|     |—Figure S8/
|     |     |—Figure S8.png
|     |     |—Figure S8 Formatting.pptx
|     |     |—Figure S8 Unlabeled.tiff
|     |     |—figure_s8_summarized_data.csv



Explanation of all files

./README.rtf
	- A summary of all files and folders for this project
./Visualization.R
	- Imports the raw data generated by the Python simulation (found in the ./output/ folder), converts the data into a plottable format, and exports the resulting figures into the relevant folder in ./Figures/
	- The R code is organized by figure number
	- R version 4.4.0 (“Puppy Cup”)
	- Imports the dependencies: 
		- ggplot2: for generating plots
		- dplyr: for data wrangling
		- tidyr: for data wrangling
./main.py
	- Entry point for both the deterministic and stochastic simulations
	- Allows the user to create and modify deterministic and/or stochastic parameter sets, then run them through the simulation
	- Comes pre-loaded with all the code necessary to generate all datasets used in Bubrig and Gibson 2025
./deterministic_unittests.py
	- Contains code which tests all critical functions and methods of the deterministic model to ensure that they behave as expected
	- Test cases are organized into classes which run all the tests necessary to ensure a single function runs correctly. For example, the TestSetFileName class verifies that the set_file_name method in ./deterministiccode/deterministic_parameters.py behaves as expected
	- Imports the dependencies:
		- unittest: for running and evaluating unit tests
./stochastic_unittests.py
	- Contains code which tests all critical functions and methods of the stochastic model to ensure that they behave as expected
	- Test cases are organized into classes which run all the tests necessary to ensure a single function runs correctly. For example, the TestSetFileName class verifies that the set_file_name method in ./stochasticcode/stochastic_parameters.py behaves as expected
	- Imports the dependencies:
		- unittest: for running and evaluating unit tests


./deterministiccode/deterministic_parameters.py
	- Interacted with through ./main.py
	- Creates an object that stores simulation parameter values
	- These objects come preloaded with default values
	- These objects come with methods so the user can change those default values, and some of these methods process parameter ranges so that the user can (for instance) run the simulation across all values of bottleneck timing from 1 to 10 with a step size of 1.
	- Imports the dependencies:
		- numpy: to generate a range of parameter values from user-inputted minimum, maximum, and step size
		- typing: to make type hints clearer for callable functions
./deterministiccode/deterministic_model.py
	- Interacted with through ./main.py
	- The only public function needed is run(), which takes a parameter object from ./deterministiccode/deterministic_parameters.py and runs the deterministic simulation with those parameters.
	- Contains all the functions necessary to explore the requested parameter space, process host birth, process parasite transmission, process any other additional processes like recovery or virulence, simulate the bottleneck process, and ultimately push the data generated to the logger module
	- Imports the dependencies:
		- numpy: to run the random number generation necessary for processing variation in bottleneck frequency and/or bottleneck severit
		- itertools: if the user has requested multiple parameters be traversed across a range of values, itertools generates the n-dimensional parameter space that the simulation will explore 
		- typing: to make type hints clearer for callable functions
./deterministiccode/logger.py
	- Not directly interacted with by the user
	- Accumulates raw data flowing from the simulation, organizes it into the appropriate columns, and ultimately writes the data to a .csv file in the ./output/ folder
	- Imports the dependency:
		- csv: to convert Python lists into the .csv file format so that data can be written to .csv files


./stochasticcode/stochastic_parameters.py
	- Interacted with through ./main.py
	- Creates an object that stores simulation parameter values
	- These objects come preloaded with default values
	- These objects come with methods so the user can change those default values, and some of these methods process parameter ranges so that the user can (for instance) run the simulation across all values of bottleneck timing from 10 to 100 with a step size of 1.
	- Imports the dependencies:
		- numpy: to generate a range of parameter values from user-inputted minimum, maximum, and step size
		- typing: to make type hints clearer for callable functions
./stochasticcode/stochastic_model.py
	- Interacted with through ./main.py
	- The only public function needed is run(), which takes a parameter object from ./stochasticcode/stochastic_parameters.py and runs the stochastic simulation with those parameters.
	- Contains all the functions necessary to explore the requested parameter space, process host birth, process parasite transmission, process any other additional processes like recovery or virulence, simulate the bottleneck process, and ultimately push the data generated to the logger module
	- Imports the dependencies:
		- numpy: to run the random number generation necessary for handling stochastic birth, transmission, etc and for handling variation in bottleneck frequency and/or bottleneck severity
		- itertools: if the user has requested multiple parameters be traversed across a range of values, itertools generates the n-dimensional parameter space that the simulation will explore 
		- typing: to make type hints clearer for callable functions
./stochasticcode/logger.py
	- Not directly interacted with by the user
	- Accumulates raw data flowing from the simulation, organizes it into the appropriate columns, and ultimately writes the data to a .csv file in the ./output/ folder
	- Imports the dependency:
		- csv: to convert Python lists into the .csv file format so that data can be written to .csv files


./output/figure_1_max_prev_data.csv
	- Raw data corresponding to Figure 1 (specifically the data represented by the black line, from simulations in which the initial prevalence was 1.0)
	- Column names and metadata:
		- Series
			- The series number begins at 1 and increments every time a bottleneck occurs
			- Can be useful for data wrangling if you need a way to group together or summarize data from all the timepoints between two successive bottleneck events
		- Timepoint
			- The simulation time point. Between timepoints, the simulation processes one time point’s worth of births, transmissions, etc.
			- Unitless
			- Starts at 0, increments by integer values, and resets back to 0 every time a bottleneck occurs
		- S
			- The state variable S, which represents the current number of susceptible hosts (i.e. are not infected but can become infected) in the population
			- Ranges from 0 to the carrying capacity (if using regulated birth) or 0 to infinity (if using exponential birth)
			- In the deterministic model, this can be a decimal value. In the stochastic model, this must be an integer value.
		- I
			- The state variable I, which represents the current number of infected hosts in the population
			- Ranges from 0 to the carrying capacity (if using regulated birth) or 0 to infinity (if using exponential birth)
			- In the deterministic model, this can be a decimal value. In the stochastic model, this must be an integer value.
		- R
			- The state variable R, which represents the current number of recovered hosts (i.e. hosts that were once infected, are no longer infected, and no longer can be infected) in the population
			- Ranges from 0 to the carrying capacity (if using regulated birth) or 0 to infinity (if using exponential birth)
			- In the deterministic model, this can be a decimal value. In the stochastic model, this must be an integer value
			- In Bubrig and Gibson 2025, this value is always zero except when briefly testing a version of the model which includes recovery
		- InitialPrevalence
			- The parasite prevalence (proportion of hosts that are infected) in the initial population before the simulation begins
			- Ranges from 0 to 1
		- BottleneckSizeMean
			- One of the parameters defining bottleneck severity
			- The (mean) number of hosts that survive each population bottleneck
			- Unit is number of hosts, should be greater than 0, and should be an integer number (decimal numbers may work, but have not been tested)
			- If the Coefficient of Variation (CV, see below) is 0, all bottlenecks will be of this size. If CV > 0, then bottleneck size will be sampled from a gamma distribution with this value as the mean
		- BottleneckSizeCV
			- One of the parameters defining bottleneck severity
			- The Coefficient of Variation which defines how spread out the distribution of bottleneck sizes is
			- Unitless
			- If 0, then all bottlenecks are of size BottleneckSizeMean
		- TimeTillBottleneckMean
			- One of the parameters defining bottleneck frequency
			- The (mean) number of timepoints that the simulation will run for before the next bottleneck occurs
			- Unit is number of timepoints, should be greater than 0, and should be an integer number
			- If the Coefficient of Variation (CV, see below) is 0, the simulation will always run with exactly TimeTillBottleneckMean time steps between bottleneck events. If CV > 0, then after each bottleneck, 
			  the number of timepoints until the next one will be sampled from a gamma distribution with this value as the mean
		- TimeTillBottleneckCV
			- One of the parameters defining bottleneck frequency
			- The Coefficient of Variation which defines how spread out the distribution of bottleneck frequency is
			- Unitless
			- If 0, then all bottlenecks occur after TimeTillBottleneckMean time steps
		- BirthRate
			- The inherent birth rate of the host population
			- Represented by b in Bubrig and Gibson 2025
			- In units of births per host per time step
			- Can theoretically range from 0 to infinity, but the default value is 0.01 (reported as 1.0 in Bubrig and Gibson 2025 by scaling all parameters values by 100)
		- CarryingCapacity
			- Only used if the BirthType is “Regulated”
			- The carrying capacity of the population; once the host population size reaches this value, the effective birth rate is zero and the population cannot grow
			- Represented by K in Bubrig and Gibson 2025
			- In units of number of hosts
			- Default value = 1000 individuals
		- BirthType
			- Has two possible values:
				- “Regulated”: indicates that the simulation was run with regulated birth, in which the birth rate of the host decreases as the population approaches carrying capacity
				- “Exponential”: indicates that the simulation was run with exponential birth, in which the birth rate is a constant
		- ParasiteFecundityEffect
			- (Not used in Bubrig and Gibson 2025)
			- Represents the percent reduction in fecundity of infected hosts compared to susceptible hosts
			- Ranges from 0 to 1
		- SDeathRate
			- (Not used in Bubrig and Gibson 2025)
			- The rate at which susceptible hosts die
			- In units of deaths per susceptible host per time step
			- Ranges from 0 to 1
		- IDeathRate
			- Referred to as “infected death rate” in Bubrig and Gibson 2025, and represented as the alpha symbol
			- The rate at which infected hosts die
			- In units of deaths per infected host per time step
			- Ranges from 0 to 1
		- RDeathRate
			- (Not used in Bubrig and Gibson 2025)
			- The rate at which recovered hosts die
			- In units of deaths per recovered host per time step
			- Ranges from 0 to 1
		- TransmissionRate
			- The transmission rate, represented by the beta symbol in Bubrig and Gibson 2025
			- Units are infections per contact (between an infected and a susceptible host) per time step
			- Ranges from 0 to 1
		- TransmissionType
			- Has two possible values:
				- “Density”: indicates that the simulation was run with density-dependent transmission
				- “Frequency”: indicates that the simulation was run with frequency-dependent transmission
		- RecoveryRate
			- The recovery rate, represented by the gamma symbol in Bubrig and Gibson 2025
			- Units are in recoveries per infected host per time step
			- Ranges from 0 to 1
			- In Bubrig and Gibson 2025, this value is always zero except when briefly testing a version of the model which includes recovery
		- FractTimestepSize
			- The size of the fractional time step that the simulation was run
			- (For improved precision, each time step in the simulation could be divided into smaller fractional time steps that the simulation could iteratively run through)
			- Must be nonzero, ranges from 0 to 1
				- Ex: a value of 0.1 means each time step was divided into 10 fractional time steps, each of size 0.1
./output/figure_1_prev_range_data.csv
	- Raw data corresponding to Figure 1 (specifically the data represented by the grey lines, from simulations in which the initial prevalence values were less than 1.0)
	- Column names and metadata:
		- (See above)
./output/figure_2_data.csv
	- Raw data corresponding to Figure 2
	- Column names and metadata:
		- (See above)
./output/figure_3_deterministic_data.csv
	- Raw data corresponding to Figure 3 (specifically the data from the model with deterministic bottlenecks, which is shown as the black lines)
	- Column names and metadata:
		- (See above)
./output/figure_3_stochastic_data.csv
	- Raw data corresponding to Figure 3 (specifically the data from the model with stochastic bottlenecks, which is shown as the grey lines)
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_4_data.csv
	- Raw data corresponding to Figure 4
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_5_data.csv
	- Raw data corresponding to Figure 5
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_s1_data.csv
	- Raw data corresponding to Figure S1
	- Column names and metadata:
		- (See above)
./output/figure_s2_exponential_ddt_data.csv
	- Raw data corresponding to Figure S2 (specifically the data from a simulation that had an exponential birth function and a density-dependent transmission function) 
	- Column names and metadata:
		- (See above)
./output/figure_s2_exponential_fdt_data.csv
	- Raw data corresponding to Figure S2 (specifically the data from a simulation that had an exponential birth function and a frequency-dependent transmission function) 
	- Column names and metadata:
		- (See above)
./output/figure_s2_regulated_ddt_data.csv
	- Raw data corresponding to Figure S2 (specifically the data from a simulation that had a regulated birth function and a density-dependent transmission function) 
	- Column names and metadata:
		- (See above)
./output/figure_s2_regulated_fdt_data.csv
	- Raw data corresponding to Figure S2 (specifically the data from a simulation that had an regulated birth function and a frequency-dependent transmission function) 
	- Column names and metadata:
		- (See above)
./output/figure_s3_recurring_bottleneck_data.csv
	- Raw data corresponding to Figure S3 (specifically the data corresponding to populations with varying recovery rate subjected to a series of recurring bottlenecks) 
	- Column names and metadata:
		- (See above)
./output/figure_s3_single_bottleneck_data.csv
	- Raw data corresponding to Figure S3 (specifically the data corresponding to populations with varying recovery rate subjected to a single bottleneck event) 
	- Column names and metadata:
		- (See above)
./output/figure_s4_recurring_bottleneck_data.csv
	- Raw data corresponding to Figure S4 (specifically the data corresponding to populations with varying virulence rate subjected to a series of recurring bottlenecks) 
	- Column names and metadata:
		- (See above)
./output/figure_s4_single_bottleneck_data.csv
	- Raw data corresponding to Figure S4 (specifically the data corresponding to populations with varying virulence rate subjected to a single bottleneck event) 
	- Column names and metadata:
		- (See above)
./output/figure_s5_01_data.csv
	- Raw data corresponding to Figure S5, specifically the part of the figure showing runs in which the transmission rate was set to 0.0001 (reported as 0.01 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
./output/figure_s5_005_data.csv
	- Raw data corresponding to Figure S5, specifically the part of the figure showing runs in which the transmission rate was set to 0.00005 (reported as 0.005 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
./output/figure_s5_0025_data.csv
	- Raw data corresponding to Figure S5, specifically the part of the figure showing runs in which the transmission rate was set to 0.000025 (reported as 0.0025 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
./output/figure_s5_00125_data.csv
	- Raw data corresponding to Figure S5, specifically the part of the figure showing runs in which the transmission rate was set to 0.0000125 (reported as 0.00125 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
./output/figure_s6_01_data.csv
	- Raw data corresponding to Figure S6, specifically the panel corresponding to simulation runs in which the transmission rate was set to 0.0001 (reported as 0.01 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_s6_005_data.csv
	- Raw data corresponding to Figure S6, specifically the panel corresponding to simulation runs in which the transmission rate was set to 0.00005 (reported as 0.005 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_s6_0025_data.csv
	- Raw data corresponding to Figure S6, specifically the panel corresponding to simulation runs in which the transmission rate was set to 0.000025 (reported as 0.0025 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_s6_00125_data.csv
	- Raw data corresponding to Figure S6, specifically the panel corresponding to simulation runs in which the transmission rate was set to 0.0000125 (reported as 0.00125 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_s7_01_data.csv
	- Raw data corresponding to Figure S7, specifically the part of the figure showing runs in which the transmission rate was set to 0.0001 (reported as 0.01 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
./output/figure_s7_005_data.csv
	- Raw data corresponding to Figure S7, specifically the part of the figure showing runs in which the transmission rate was set to 0.00005 (reported as 0.005 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
./output/figure_s7_0025_data.csv
	- Raw data corresponding to Figure S7, specifically the part of the figure showing runs in which the transmission rate was set to 0.000025 (reported as 0.0025 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
./output/figure_s7_00125_data.csv
	- Raw data corresponding to Figure S7, specifically the part of the figure showing runs in which the transmission rate was set to 0.0000125 (reported as 0.00125 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
./output/figure_s8_01_data.csv
	- Raw data corresponding to Figure S8, specifically the panel corresponding to simulation runs in which the transmission rate was set to 0.0001 (reported as 0.01 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_s8_005_data.csv
	- Raw data corresponding to Figure S8, specifically the panel corresponding to simulation runs in which the transmission rate was set to 0.00005 (reported as 0.005 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_s8_0025_data.csv
	- Raw data corresponding to Figure S8, specifically the panel corresponding to simulation runs in which the transmission rate was set to 0.000025 (reported as 0.0025 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated
./output/figure_s8_00125_data.csv
	- Raw data corresponding to Figure S8, specifically the panel corresponding to simulation runs in which the transmission rate was set to 0.0000125 (reported as 0.00125 in Bubrig and Gibson 2025)
	- Column names and metadata:
		- (See above)
		- Also includes Rep
			- An identifying integer which corresponds to which stochastic replicate the data come from
			- For each unique combination of parameters, Rep starts at 0 and increments every time that combination of parameters is fully replicated

./Figures/Figure 1/2 Panel.tiff
	 - An outputted figure that shows data from a population experiencing bottlenecks that occur every 200 time steps (reported as 2 in Bubrig and Gibson 2025)
./Figures/Figure 1/3 Panel.tiff
	- An outputted figure that shows data from a population experiencing bottlenecks that occur every 300 time steps (reported as 3 in Bubrig and Gibson 2025)
./Figures/Figure 1/4 Panel.tiff
	- An outputted figure that shows data from a population experiencing bottlenecks that occur every 400 time steps (reported as 4 in Bubrig and Gibson 2025)
./Figures/Figure 1/Empty Panels.tiff
	- An outputted figure that has labeled axes with three empty panels stacked vertically
./Figures/Figure 1/Figure 1.png
	- The formatted figure in which all three time series figures have been put into vertically-stacked panels
./Figures/Figure 1/Figure 1 Formatting.pptx
	- The Powerpoint file used to insert 2 Panel.tiff, 3 Panel.tiff, and 4 Panel.tiff into the empty panels of Empty Panels.tiff

./Figures/Figure 2/Figure 2.png
	- The formatted figure which includes labels for pmax and pmin
./Figures/Figure 2/Figure 2 Formatting.pptx
	- The Powerpoint file used to add the labels pmax and pmin to Figure 2
./Figures/Figure 2/Figure 2 Unlabeled.tiff
	 - The outputted figure that shows pmax and pmin across a range of bottleneck frequencies. Does not include labels

./Figures/Figure 3/2 Panel.tiff
	- An outputted figure that shows data from the stochastic model where a population experiences bottlenecks that occur every 200 time steps (reported as 2 in Bubrig and Gibson 2025)
./Figures/Figure 3/3 Panel.tiff
	- An outputted figure that shows data from the stochastic model where a population experiences bottlenecks that occur every 300 time steps (reported as 3 in Bubrig and Gibson 2025)
./Figures/Figure 3/4 Panel.tiff
	- An outputted figure that shows data from the stochastic model where a population experiences bottlenecks that occur every 400 time steps (reported as 4 in Bubrig and Gibson 2025)
./Figures/Figure 3/Empty Panels.tiff
	- An outputted figure that has labeled axes with three empty panels stacked vertically
./Figures/Figure 3/Figure 3.png
	- The formatted figure in which all three time series figures have been put into vertically-stacked panels
./Figures/Figure 3/Figure 3 Formatting.pptx
	- The Powerpoint file used to insert 2 Panel.tiff, 3 Panel.tiff, and 4 Panel.tiff into the empty panels of Empty Panels.tiff

./Figures/Figure 4/Figure 4.tiff
	- The outputted Figure 4
./Figures/Figure 4/figure_4_summarized_data.csv
	- A dataset which is a condensed version of ./output/figure_4_data.csv
	- Contains columns already explained above, plus:
		- TotalReps
			The total number of stochastic replicates that were run for this combination of TimeTillBottleneckMean and TimeTillBottleneckCV
		- ExtinctionCount
			The number of stochastic replicates of this parameter combination that resulted in parasite extinction, i.e. where by the end of the series of recurring bottlenecks, parasite prevalence = 0
		- ExtinctionProbability
			ExtinctionCount divided by TotalReps
	- ./output/figure_4_data.csv is a large file (~1.17 GB) and can be a pain to load into R. Once loaded into R however, the dataset is wrangled into a much smaller format for plotting purposes, 
	   so this .csv file can be loaded directly into R and visualized to skip the import of the large raw data file

./Figures/Figure 5/Figure 5.tiff
	- The outputted Figure 5
./Figures/Figure 5/figure_5_summarized_data.csv
	- A dataset which is a condensed version of ./output/figure_5_data.csv
	- Contains columns already explained above, plus:
		- TotalReps
			The total number of stochastic replicates that were run for this combination of BottleneckSizeMean and BottleneckSizeCV
		- ExtinctionCount
			The number of stochastic replicates of this parameter combination that resulted in parasite extinction, i.e. where by the end of the series of recurring bottlenecks, parasite prevalence = 0
		- ExtinctionProbability
			ExtinctionCount divided by TotalReps
	- ./output/figure_5_data.csv is a large file (~924 MB) and can be a pain to load into R. Once loaded into R however, the dataset is wrangled into a much smaller format for plotting purposes, 
	   so this .csv file can be loaded directly into R and visualized to skip the import of the large raw data file

./Figures/Figure S1/Figure S1.png
	- The formatted figure which includes a label for bottleneck frequency
./Figures/Figure S1/Figure S1 Formatting.pptx
	- The Powerpoint file used to add the label to Figure S1
./Figures/Figure S1/Figure S1 Unlabelled.tiff
	- An outputted figure demonstrating the effect of bottlenecks on the host population. Does not include a label for bottleneck frequency

./Figures/Figure S2/Figure S2.tiff
	- The outputted Figure S2

./Figures/Figure S3/Figure S3.png
	- The formatted figure S3 in which the panels from the single bottleneck simulation and the recurring bottleneck simulation are combined with a legend
./Figures/Figure S3/Figure S3 Formatting.pptx
	- The Powerpoint file used to combine the single bottleneck, recurring bottleneck, and SIR panels
./Figures/Figure S3/Figure S3 Recurring Bottleneck Panel.tiff
	- The outputted figure panel of the data from recurring bottlenecks
./Figures/Figure S3/Figure S3 Single Bottleneck Panel.tiff
	- The outputted figure panel of the data from a single bottleneck event
./Figures/Figure S3/Figure S3 SIR Panel.tiff
	- The outputted figure panel of the data from a single series of recurring bottlenecks, broken down into S, I, and R components

./Figures/Figure S4/Figure S4.png
	- The formatted figure S4 in which the panels from the single bottleneck simulation and the recurring bottleneck simulation are combined with a single legend
./Figures/Figure S4/Figure S4 Formatting.pptx
	- The Powerpoint file used to combine the single bottleneck and recurring bottleneck panels
./Figures/Figure S4/Figure S4 Recurring Bottleneck Panel.tiff
	- The outputted figure panel of the data from recurring bottlenecks
./Figures/Figure S4/Figure S4 Single Bottleneck Panel.tiff
	- The outputted figure panel of the data from a single bottleneck event

./Figures/Figure S5/Figure S5.tiff
	- The outputted Figure S5

./Figures/Figure S6/Figure S6.png
	- The formatted figure which includes a label for parasite transmission rate
./Figures/Figure S6/Figure S6 Formatting.pptx
	- The Powerpoint file used to add the label to Figure S6
./Figures/Figure S6/Figure S6 Unlabelled.tiff
	- An outputted figure. Does not include a label for parasite transmission rate
./Figures/Figure S6/figure_s6_summarized_data.csv
	- A dataset which is a condensed version of ./output/figure_s6_01_data.csv, ./output/figure_s6_005_data.csv, ./output/figure_s6_0025_data.csv, and ./output/figure_s6_00125_data.csv
	- Contains columns already explained above, plus:
		- TotalReps
			The total number of stochastic replicates that were run for this combination of BottleneckSizeMean and BottleneckSizeCV
		- ExtinctionCount
			The number of stochastic replicates of this parameter combination that resulted in parasite extinction, i.e. where by the end of the series of recurring bottlenecks, parasite prevalence = 0
		- ExtinctionProbability
			ExtinctionCount divided by TotalReps
	- The raw data files in ./output are a large files (~1.3 GB each) and can be a pain to load into R. Once loaded into R however, the combined dataset is wrangled into a much smaller format for plotting purposes, 
	   so this .csv file can be loaded directly into R and visualized to skip the import of the large raw data file

./Figures/Figure S7/Figure S7.tiff
	- The outputted Figure S7

./Figures/Figure S8/Figure S8.png
	- The formatted figure which includes a label for parasite transmission rate
./Figures/Figure S8/Figure S8 Formatting.pptx
	- The Powerpoint file used to add the label to Figure S8
./Figures/Figure S8/Figure S8 Unlabelled.tiff
	- An outputted figure. Does not include a label for parasite transmission rate
./Figures/Figure S8/figure_s8_summarized_data.csv
	- A dataset which is a condensed version of ./output/figure_s8_01_data.csv, ./output/figure_s8_005_data.csv, ./output/figure_s8_0025_data.csv, and ./output/figure_s8_00125_data.csv
	- Contains columns already explained above, plus:
		- TotalReps
			The total number of stochastic replicates that were run for this combination of BottleneckSizeMean and BottleneckSizeCV
		- ExtinctionCount
			The number of stochastic replicates of this parameter combination that resulted in parasite extinction, i.e. where by the end of the series of recurring bottlenecks, parasite prevalence = 0
		- ExtinctionProbability
			ExtinctionCount divided by TotalReps
	- The raw data files in ./output are a large files (~750 MB each) and can be a pain to load into R. Once loaded into R however, the combined dataset is wrangled into a much smaller format for plotting purposes, 
	   so this .csv file can be loaded directly into R and visualized to skip the import of the large raw data file
