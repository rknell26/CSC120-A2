"""   
Filename: computer.py
Description: The computer class, which contains code pertaining to the computer(s) 
            created by the program, including their attributes and methods 
            to update price and operating system, and to print details about them.
     Author: Rachel Knell
     Peers: Chloe Wahl-Dussle
     Date: 11 February 2023
"""

class computer:

    # What attributes will it need?
    name: str
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, name, description, pro_type, hd_cap, mem, os, year, price):
        self.name = name
        self.description = description
        self.pro_type = pro_type
        self.hd_cap = hd_cap
        self.mem = mem
        self.os = os
        self.year = year
        self.price = price 

        # What methods will you need?

    def reprice (self, new_price):
            self.price = new_price
    


    def updateOS (self, new_os):  
            self.os = new_os
        
    def print_details (self):
        print(self.name)
        print(self.description)
        print(self.pro_type)
        print(self.hd_cap)
        print(self.mem)
        print(self.os)
        print(self.year)
        print(self.price)

   