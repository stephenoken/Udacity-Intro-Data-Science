from datetime import datetime
from functools import reduce
from util import contains, write_to_file

def generate_output(key, value_tuple):
    date_str = value_tuple[1].strftime("%Y-%m-%d %H:%M:%S")
    return "{}\t{}\t{}\n".format(key, date_str, str(value_tuple[0]))

def calculate_busiest_time(key_values_dict, key_value):
    key, value = key_value.strip().split("\t", 1)
    entries, date, time = value.strip().split('\t')
    entries_num = float(entries)
    entry_time = datetime.strptime(date + "T" + time, "%Y-%m-%dT%H:%M:%S")
    keys = list(key_values_dict)
    current_count = key_values_dict[key] if contains(keys, key) else (0.0, datetime(1970,1,1))
    entry_high = current_count if current_count[0] > entries_num or (current_count[0] == entries_num and current_count[1] > entry_time) else (entries_num, entry_time)
    key_values_dict[key] = entry_high
    return key_values_dict


def reducer(ridership_file):
    '''
    Write a reducer that will compute the busiest date and time (that is, the 
    date and time with the most entries) for each turnstile unit. Ties should 
    be broken in favor of datetimes that are later on in the month of May. You 
    may assume that the contents of the reducer will be sorted so that all entries 
    corresponding to a given UNIT will be grouped together.
    
    The reducer should print its output with the UNIT name, the datetime (which 
    is the DATEn followed by the TIMEn column, separated by a single space), and 
    the number of entries at this datetime, separated by tabs.

    For example, the output of the reducer should look like this:
    R001    2011-05-11 17:00:00	   31213.0
    R002	2011-05-12 21:00:00	   4295.0
    R003	2011-05-05 12:00:00	   995.0
    R004	2011-05-12 12:00:00	   2318.0
    R005	2011-05-10 12:00:00	   2705.0
    R006	2011-05-25 12:00:00	   2784.0
    R007	2011-05-10 12:00:00	   1763.0
    R008	2011-05-12 12:00:00	   1724.0
    R009	2011-05-05 12:00:00	   1230.0
    R010	2011-05-09 18:00:00	   30916.0
    ...
    ...

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    with open(ridership_file) as ridership_data:
        output_filename = "./subway_busiest_hour.txt"
        ridership_dict = reduce(calculate_busiest_time, [data for data in ridership_data], {})
        [write_to_file(output_filename, generate_output(k, v)) for k, v in ridership_dict.items()]


if __name__ == "__main__":
    reducer("./subway_ridership_by_hour_and_unit.txt")
