from functools import reduce
from util import contains, count_entries, write_to_file


def reducer(ridership_file):
    '''
    Given the output of the mapper for this exercise, the reducer should PRINT 
    (not return) one line per UNIT along with the total number of ENTRIESn_hourly 
    over the course of May (which is the duration of our data), separated by a tab.
    An example output row from the reducer might look like this: 'R001\t500625.0'

    You can assume that the input to the reducer is sorted such that all rows
    corresponding to a particular UNIT are grouped together.

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    with open(ridership_file) as ridership_data:
        output_filename = "./subway_ridership_count.txt"
        ridership_dict = reduce(count_entries, [data for data in ridership_data], {})
        [write_to_file(output_filename, "{}\t{}\n".format(k, v)) for k, v in ridership_dict.items()]


if __name__ == "__main__":
    reducer("./subway_ridership.txt")
