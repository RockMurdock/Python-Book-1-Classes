from building import Building
from city import City

building_one = Building("123 Abc Street", 99)
building_two = Building("456 Abc Street", 98)
building_three = Building("789 Abc Street", 97)
building_four = Building("101112 Abc Stree", 96)
building_five = Building("131415 Abc Street", 95)

building_one.purchase("Ashley")
building_two.purchase("Dorothy")
building_three.purchase("Coleman")
building_four.purchase("Dustin")
building_five.purchase("Dr.Mundo")

building_one.construct()
building_two.construct()
building_three.construct()
building_four.construct()
building_five.construct()

meglopolis = City("Megalopolis", "Cody", "1986")

meglopolis.addBuilding(building_one)
meglopolis.addBuilding(building_two)
meglopolis.addBuilding(building_three)
meglopolis.addBuilding(building_four)
meglopolis.addBuilding(building_five)

for building in meglopolis.buildings:
    print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.\n')