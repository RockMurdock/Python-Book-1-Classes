"""
In this exercise, you are going to define your own Building type and create several instances
of it to design your own virtual city. Create a class named Building in the building.py file 
and define the following fields, properties, and methods.

designer - It will hold your name.
date_constructed - This will hold the exact time the building was created.
owner - This will store the same of the person who owns the building.
address
stories

Define a construct() method. The method's logic should set the date_constructed 
field's value to datetime.datetime.now(). You will need to have import datetime at the 
top of your file.

Define a purchase() method. The method should accept a single string argument of the 
name of the person purchasing a building. The method should take that string and assign it 
to the owner property.

"""
import datetime

class Building:

# Define your __init__ method to accept two arguments
# address
# stories
   
    def __init__(self, address, stories):
        self.designer = "Cody Murdock"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()
    
    def purchase(self, name):
        self.owner = name

    def building_report(self):
        print(f'{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.\n')

# Once defined this way, you can send those values as parameters when you create each instance

#  eight_hundred_eighth = Building("800 8th Street", 12)

# Create 5 building instances

building_one = Building("123 Abc Street", 99)
building_two = Building("456 Abc Street", 98)
building_three = Building("789 Abc Street", 97)
building_four = Building("101112 Abc Stree", 96)
building_five = Building("131415 Abc Street", 95)

#Have each one get purchased by a real estate magnate

building_one.purchase("Ashley")
building_two.purchase("Dorothy")
building_three.purchase("Coleman")
building_four.purchase("Dustin")
building_five.purchase("Dr.Mundo")

# After purchased, construct each one

building_one.construct()
building_two.construct()
building_three.construct()
building_four.construct()
building_five.construct()

# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.

# building_one.building_report()
# building_two.building_report()
# building_three.building_report()
# building_four.building_report()
# building_five.building_report()