
class Customer: 
    def __init__(self, title, first_name, last_name, age, ccn, id=None):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ccn = ccn
        self.id = id 


    def print_summary(self):
        if self.title == None:
            print(f"{self.first_name} {self.last_name} is {self.age} and this is their creditcard number - {self.ccn}. G' Day!")
        else:
            print(f"{self.title} {self.first_name} {self.last_name} is {self.age} and this is their creditcard number - {self.ccn}. G' Day!")
# mr. roy lewis,1922-12-30,"472 Marian ridges,Smithmouth,TQ5R 7UW",collinsalexander@hotmail.com,"472 Marian ridges,Smithmouth,TQ5R 7UW",630410320802
