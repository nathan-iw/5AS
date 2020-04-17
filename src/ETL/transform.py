    ## Transform ###
import src.ETL.customer as custo
from src.ETL.extract import csv_load 
from datetime import date


title_list = ["miss","ms","mrs","mr","dr"]

imp_customers = csv_load("customer.csv")

def name_breaker(name): # Function to reformat names
    breaking_name = name.strip().lower().replace(".", "")
    broken_name = breaking_name.split(" ")
    last_name = broken_name[-1].title()
    if broken_name[0] in title_list:
        title = broken_name[0].capitalize()
        first_name = broken_name[1].capitalize()
    else:
        title = None 
        first_name = broken_name[0].capitalize()
    return (title, first_name, last_name)

# Name,DOB,Address,email,billing address,ccn
def process_customers(data):
    customer_list=[]
    for row in data:
        if len(row) == 0 or row[0] == "Name":
            continue
        try:
            age = age_gen(row[1])
        except ValueError:
            continue
        title, first_name, last_name = name_breaker(row[0])
        customer_tuple = (title, first_name, last_name, age, card_masker(row[-1]))
        customer_list.append(customer_tuple)
    return customer_list
        
def card_masker(card):
    if len(card) > 4:
        digits = card.replace(card[:-4], (len(card)-4) * "X") # X's out everything othet than the last 4 digits
        return(digits)
    else: 
        return("invalid ccn")

def age_gen(dob):
    days_in_year = 365.2425
    y, m, d = int(dob[:4]), int(dob[5:7]), int(dob[-2:])
    birthDate = date(y, m, d)
    age = int((date.today() - birthDate).days / days_in_year)
    return age
    
if __name__ == "__main__":
    print(digits)



# mr. roy lewis,1922-12-30,"472 Marian ridges,Smithmouth,TQ5R 7UW",collinsalexander@hotmail.com,"472 Marian ridges,Smithmouth,TQ5R 7UW",630410320802
