import csv


def write_key_value_pairs(aadhaar_dict):
    district = aadhaar_dict["District"]
    generated_num = aadhaar_dict["Aadhaar generated"]
    with open('generated_aadhaar.txt', 'a') as generated_file:
        generated_file.write("{}\t{}\n".format(district, generated_num))
    
    
def mapper(file_path):

    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the 
    #commas, and emit (i.e. print) a key-value pair containing the 
    #district (not state) and Aadhaar generated, separated by a tab. 
    #Skip rows without the correct number of tokens and also skip 
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    with open(file_path) as csv_file:
        aadhaar_data = csv.DictReader(csv_file)
        [write_key_value_pairs(data) for data in aadhaar_data]

mapper("./aadhaar_data.csv")
