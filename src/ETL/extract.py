### EXTRACT ###

import csv 

def csv_load(file):
    customer_list = []
    try:
        with open(file,"r") as csv_file:
           rows = csv.reader(csv_file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
           for row in rows:
                customer_list.append(row)
        return customer_list
    except Exception as error:
        print(f" error {error}")



