### Transform ###

title_list = ["miss","ms","mrs","mr","dr"]

# from extract import csv_load 

# customer_list = csv_load("customer.csv")

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









# mr. roy lewis,1922-12-30,"472 Marian ridges,Smithmouth,TQ5R 7UW",collinsalexander@hotmail.com,"472 Marian ridges,Smithmouth,TQ5R 7UW",630410320802
