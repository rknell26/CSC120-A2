"""   
Filename: oo_resale_shop.py
Description: The ResaleShop class and and main() function. 
            The ResaleShop class contains code pertaining to the shop's inventory,
            including methods to buy, sell, and refurbish computers, and to print inventory. 
            The main() function runs the shop and has it complete the ResaleShop functions.
     Author: Rachel Knell
     Peers: Chloe Wahl-Dussle
     Date: 11 February 2023
"""

from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__ (self, inventory):
        self.inventory = inventory

     
    # What methods will you need?

    def buy (self, comp):
            print("Buying", comp.name)
            print("Adding to inventory...")
            self.inventory.append(comp)
            print("Done.\n")


    def sell (self, comp):
        if comp in self.inventory:
            print("Selling Item:", comp.name)
            self.inventory.remove(comp)
        else:
            print("Error")


    def print_inventory (self):
        if self.inventory != []:
            print("Checking inventory...")
        # For each item
            for comp in self.inventory:
            # Print its details
                comp.print_details()
            print("Done.\n")
        else:
            print("No inventory to display.")


    def refurbish (self, comp, new_os):
        if comp in self.inventory:
            print("Refurbishing Item:", comp.name)
            print("Updating inventory...")
            if comp.year < 2000:
                comp.reprice(0) # too old to sell, donation only
            elif comp.year < 2012:
                comp.reprice(250) # heavily-discounted price on machines 10+ years old
            elif comp.year < 2018:
                comp.reprice(550) # discounted price on machines 4-to-10 year old machines
            else:
                comp.reprice(1000) # recent stuff
                     

            if new_os is not None:
                comp.updateOS(new_os) # update details after installing new OS
            print("Done.\n")
        else:
            print("Error")
        

def main():

    

    # First, let's make a computer
    computer1 = computer("Mac-kenzie", "Mac Pro (Late 2013)", 
        "3.5 GHc 6-Core Intel Xeon E5", 
        1024, 64, "macOS Big Sur", 2013, 1500)

    
    
    
    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    
    
    # Add it to the resale store's inventory
    
    ResaleShop.buy(ResaleShop, computer1)

    
    
    
    # Make sure it worked by checking inventory
    
    ResaleShop.print_inventory(ResaleShop)
    
    

    # Now, let's refurbish it
    
    ResaleShop.refurbish(ResaleShop, computer1, "OS 89")
  
    # Make sure it worked by checking inventory
   
    ResaleShop.print_inventory(ResaleShop)
 
    
    # Now, let's sell it!

    ResaleShop.sell(ResaleShop, computer1)
    
    # Make sure it worked by checking inventory
  
    ResaleShop.print_inventory(ResaleShop)
  

    

# Calls the main() function when this file is run
if __name__ == "__main__": main()

