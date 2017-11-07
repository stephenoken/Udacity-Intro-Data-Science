import csv
from functools import reduce

def build_turnstile_data(row_header, row_body):
    new_row_body = row_body[:5]
    remaining_row_body = row_body[5:]
    new_row = [row_header + new_row_body]
    return new_row + build_turnstile_data(row_header, remaining_row_body) if len(remaining_row_body) >= 5 else new_row

def extract_turnstile_data(row):
    row_head = row[:3]
    row_body = row[3:]
    return build_turnstile_data(row_head, row_body)


def parse_csv(file_name):
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile)
        reformatted_data = reduce(lambda xs, x: xs + extract_turnstile_data(x), reader, [])
        # print(reformatted_data)
        with open("updated_" + file_name, 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(reformatted_data)


def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    [parse_csv(name) for name in filenames]


fix_turnstile_data(['turnstile_110507.txt'])
