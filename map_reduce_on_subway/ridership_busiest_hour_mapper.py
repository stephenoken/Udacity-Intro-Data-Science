import csv
from util import write_key_value_pairs

def transform_subway_data(data):
    # fog_status = "{}fog".format('' if float(data["fog"]) == 1. else 'no')
    # rain_status = "{}rain".format('' if float(data["rain"]) == 1. else 'no')
    # data["weather_status"] = "{}-{}".format(fog_status, rain_status)
    return data


def mapper(csv_filename):
    """
    In this exercise, for each turnstile unit, you will determine the date and time 
    (in the span of this data set) at which the most people entered through the unit.
    
    The input to the mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise. You can check out the csv and its structure below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

    For each line, the mapper should return the UNIT, ENTRIESn_hourly, DATEn, and 
    TIMEn columns, separated by tabs. For example:
    'R001\t100000.0\t2011-05-01\t01:00:00'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    """
    with open(csv_filename) as csv_file:
        data = csv.DictReader(csv_file)
        file_name = "subway_ridership_by_hour_and_unit.txt"
        keys = ["UNIT", "ENTRIESn_hourly", "DATEn", "TIMEn"]
        [write_key_value_pairs(file_name, transform_subway_data(x), *keys) for x in data]


if __name__ == "__main__":
    mapper("./turnstile_data_master_with_weather.csv")
