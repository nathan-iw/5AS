### Transform ###
import src.ETL.customer as custo
from src.ETL.extract import csv_load 

title_list = ["miss","ms","mrs","mr","dr"]

imp_customers = csv_load("customer.csv")

def name_breaker(name):
    breaking_name = name.strip().lower().replace(".", "")
    broken_name = breaking_name.split(" ")
    last_name = broken_name[-1].capitalize()
    if broken_name[0] in title_list:
        title = broken_name[0].capitalize()
        first_name = broken_name[1].capitalize()
    else:
        title = None 
        first_name = broken_name[0].capitalize()
    return (title,first_name,last_name)

print(name_breaker("Martin lewis"))
my_list = ["1", "2", "3"]
my_list.append("4")
my_tuple = (1,2,3)
print(my_tuple[1])


def process_customers(data):
    customer_list=[]
    for row in data:
        arguments = name_breaker(row[0])
        new_cust = custo.Customer(arguments[0],arguments[1],arguments[2])
        customer_list.append(new_cust)
    return customer_list
        


# mr. roy lewis,1922-12-30,"472 Marian ridges,Smithmouth,TQ5R 7UW",collinsalexander@hotmail.com,"472 Marian ridges,Smithmouth,TQ5R 7UW",630410320802
