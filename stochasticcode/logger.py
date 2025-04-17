'''This module contains a single class Dataframe, which stores data column names, 
stores values that should remain constant for all rows, logs incoming data from
the model, and then outputs the full dataframe to a .csv file in the output
folder.

Within the Dataframe class, there are four methods:
__init__
    Initializes a new dataframe with some default set-up values and empty
    storage that can accept new data

add_constant_data
    Pre-stores column names and values for parameters that are not expected to 
    change across timepoints in a simulation run. For instance, the birth rate
    should be constant within a run of the simulation, so this only needs to be
    pushed to the Dataframe class once at the beginning of the run.

log_data
    Logs several rows of new data coming from the simulation. These data include
    the stochastic replicate, the series (run of the simulation), timepoint 
    number, and the values for the state variables S, I, and R. This method also 
    checks whether it should ignore the incoming data (i.e. if the simulation is 
    in the middle of a "burn in" where data doesn't need to be ouputed yet)

write_data
    Outputs the accumulated data into a .csv file in the output folder
'''

import csv

class Dataframe:
    def __init__(self, file_name: str) -> None:
        '''Initializes a new dataframe with some default set-up values and empty
        storage that can accept new data

        Explanation of attributes
        ---------

        file_name: str
            The desired name of the output .csv file (minus the ".csv" 
            extension). Note that if file_name is identical to an existing .csv
            file in the output folder, that file will be overwritten.

        VARIABLE_COLUMN_NAMES: list[str]
            A list of column names specifically for variables that are expected
            to change row-to-row or series-to-series. Each column name is a string.
            The defaults are "Rep", "Series", "Timepoint", "S", "I", and "R"

        CONSTANT_COLUMN_NAMES: list[str]
            A list of column names specifically for variables that are expected
            to stay the same row-to-row, such as the birth rate or the mean
            bottleneck size. Each column name is a string.

        constant_data: dict
            A dictionary of key-value pairs which stores the values of
            parameters that are expected to stay the same row-to-row. Each element
            holds one key (the column name) and one value (the value of the variable).
            For instance, there might be an element of the dictionary that has 
            the key "Birth Rate" (a string) and the value 0.05 (a float). These 
            constant data only need to be stored here once, then added to the 
            dataframe at the end.

        data_rows: list[dict]
            A list where each element is a dictionary of key-value pairs storing
            data. Each element (dictionary) represented one row of data in the
            final output .csv file. Within a dictionary, the key is the column
            name and the value is the value of the variable corresponding to that
            column. As data flows in from the simulation, those rows of data will
            be tacked onto the end of this list.
        '''
        
        self.file_name: str = file_name
        self.VARIABLE_COLUMN_NAMES: list[str] = ["Rep",
                                                 "Series",
                                                 "Timepoint",
                                                 "S", 
                                                 "I",
                                                 "R"]
        self.CONSTANT_COLUMN_NAMES: list[str] = []
        self.constant_data: dict = {}
        self.data_rows: list[dict] = []

    def add_constant_data(self, constants: dict) -> None:
        '''Takes in and stores column names and variable values for parameters
        that are not expected to change row-to-row, e.g. birth rate. Only needs
        to be called once at the beginning of working with a new parameter set.

        constants: dict
            Each element holds one key (the column name) and one value (the value 
            of the variable corresponding to that column). For instance, there 
            might be an element of the dictionary that has the key "Birth Rate" 
            (a string) and the value 0.05 (a float).
        '''
        self.CONSTANT_COLUMN_NAMES = list(constants.keys())
        self.constant_data = constants
    
    def log_data(self, is_logging: bool, new_data: list[list]) -> None:
        '''Logs several rows of new data coming from the simulation. These data 
        include the stochastic replicate, the series (run of the simulation), 
        timepoint number, and the values for the state variables S, I, and R. 
        This method also checks whether it should ignore the incoming data 
        (i.e. if the simulation is in the middle of a "burn in" where data 
        doesn't need to be stored yet)

        is_logging: bool
            If True, this means that the simulation is out of its burn-in period
            (or there was no burn in) and the data from the simulation should be
            stored for eventual output. If False, the simulation is still within
            a burn-in period and the data coming from the simulation can be
            ignored.

        new_data: list[list]
            Simulation data that may or may not be stored. Each element in the 
            list corresponds to a row of data (i.e. a timepoint). Each element
            is another list, in which each element is--in order--the Rep, the 
            Series, the Timepoint, and then the values of the state variables 
            S, I, and R (corresponding to the ordering of VARIABLE_COLUMN_NAMES).
        '''
        if not is_logging:
            return
        if new_data is False:
            return
        
        for row in new_data:
            data_dict = {}
            for column_index in range(len(row)):
                column_name = self.VARIABLE_COLUMN_NAMES[column_index]
                value = row[column_index]
                data_dict[column_name] = value
            data_dict.update(self.constant_data)
            self.data_rows.append(data_dict)
    
    def write_data(self) -> None:
        '''Writes the data stored in the data_rows list to a .csv file in the
        output folder. The column names in the .csv file will be the column names
        stored in the VARIABLE_COLUMN_NAMES list and the CONSTANT_COLUMN_NAMES
        list.
        '''
        with open(f'output/{self.file_name}.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames = self.VARIABLE_COLUMN_NAMES +
                                                    self.CONSTANT_COLUMN_NAMES)
            writer.writeheader()
            writer.writerows(self.data_rows)
