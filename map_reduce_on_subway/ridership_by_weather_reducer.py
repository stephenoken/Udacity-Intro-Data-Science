from util import write_to_file
from functools import reduce


def calculate_ridership(tallied_sub_dict, subway_data):
    k, v = subway_data.strip().split("\t")
    current_pax_num = tallied_sub_dict[k][0]
    current_count = tallied_sub_dict[k][1]
    tallied_sub_dict[k] = (current_pax_num + float(v), current_count + 1)
    return tallied_sub_dict

def partition_weather(subway_weather_data):
    initial_dict = {
            "fog-rain": (0.0, 0.0),
            "fog-norain": (0.0, 0.0),
            "nofog-rain": (0.0, 0.0),
            "nofog-norain": (0.0, 0.0)
        }
    return reduce(calculate_ridership, subway_weather_data, initial_dict)
    

def reducer(filename):
    '''
    Given the output of the mapper for this assignment, the reducer should
    print one row per weather type, along with the average value of
    ENTRIESn_hourly for that weather type, separated by a tab. You can assume
    that the input to the reducer will be sorted by weather type, such that all
    entries corresponding to a given weather type will be grouped together.

    In order to compute the average value of ENTRIESn_hourly, you'll need to
    keep track of both the total riders per weather type and the number of
    hours with that weather type. That's why we've initialized the variable 
    riders and num_hours below. Feel free to use a different data structure in 
    your solution, though.

    An example output row might look like this:
    'fog-norain\t1105.32467557'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''
    with open(filename) as subway_weather_data:
        tallied_sub_data = partition_weather(subway_weather_data)
        print(tallied_sub_data)
        output_filename = "subway_weather_ridership_count.txt"
        [write_to_file(output_filename, "{}\t{}\n".format(k, v[0]/v[1])) for k, v in tallied_sub_data.items()]


if __name__ == "__main__":
    reducer("./subway_weather_ridership.txt")
