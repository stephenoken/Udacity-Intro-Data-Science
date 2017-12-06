from functools import reduce
import sys
import logging


def write_to_file(content):
    with open("./generated_aadhaar_count.txt", "a") as text_file:
        text_file.write(content)

def contains(keys, key):
    return keys.count(key) > 0
    
    
def count_entries(key_values_dict, key_value):
    key, value = key_value.strip().split("\t")
    keys = list(key_values_dict.keys())
    count = key_values_dict[key] + float(value) if contains(keys, key) else float(value)
    key_values_dict[key] = count
    return key_values_dict
    
def reducer(generated_aadhaar_filename):
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    with open(generated_aadhaar_filename) as generated_file:
        adhaar_gen_dict = reduce(count_entries, [line for line in generated_file], {})
        [write_to_file("{}\t{}\n".format(k, v)) for k, v in adhaar_gen_dict.items()]
        

reducer("./generated_aadhaar.txt")
