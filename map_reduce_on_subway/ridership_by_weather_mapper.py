import csv
from util import write_key_value_pairs

def transform_subway_data(data):
    fog_status = "{}fog".format('' if float(data["fog"]) == 1. else 'no')
    rain_status = "{}rain".format('' if float(data["rain"]) == 1. else 'no')
    data["weather_status"] = "{}-{}".format(fog_status, rain_status)
    return data


def mapper(csv_filename):
    '''
    For this exercise, compute the average value of the ENTRIESn_hourly column 
    for different weather types. Weather type will be defined based on the 
    combination of the columns fog and rain (which are boolean values).
    For example, one output of our reducer would be the average hourly entries 
    across all hours when it was raining but not foggy.

    Each line of input will be a row from our final Subway-MTA dataset in csv format.
    You can check out the input csv file and its structure below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
    
    Note that this is a comma-separated file.

    This mapper should PRINT (not return) the weather type as the key (use the 
    given helper function to format the weather type correctly) and the number in 
    the ENTRIESn_hourly column as the value. They should be separated by a tab.
    For example: 'fog-norain\t12345'
    
    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    # Takes in variables indicating whether it is foggy and/or rainy and
    # returns a formatted key that you should output.  The variables passed in
    # can be booleans, ints (0 for false and 1 for true) or floats (0.0 for
    # false and 1.0 for true), but the strings '0.0' and '1.0' will not work,
    # so make sure you convert these values to an appropriate type before
    # calling the function.
    with open(csv_filename) as csv_file:
        data = csv.DictReader(csv_file)
        file_name = "subway_weather_ridership.txt"
        [write_key_value_pairs(file_name, transform_subway_data(x), "weather_status", "ENTRIESn_hourly") for x in data]


if __name__ == "__main__":
    mapper("./turnstile_data_master_with_weather.csv")
