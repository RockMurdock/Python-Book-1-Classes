# Create an Employee type that contains information about employees 
# of a company. Each employee must have a name, job title, and 
# employment start date.

class Employee:
    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

# Create a Company type that employees can work for. A company should have 
# a business name, address, and industry type.

class Company:
    def __init__(self, name, address, industry_type):
        self.name = name
        self.address = address
        self.type = industry_type
        self.employees = list()

    def hire(self, employee):
        self.employees.append(employee)

    def report(self):
        print(f"{self.name} is in the {self.type} industry and has the following empployees:")
        for worker in self.employees:
            print(f"    * {worker.name}")

# Create two companies, and 5 people who want to work for them.

warehouse = Company("Murdock's Warehouse", "420 Murdock Way", "Hemp Distributor")
store = Company("Murdock's Hemp", "840 Murdock Way", "Hemp Retail")
ashley = Employee("Ashley Murdock", "Warehouse Manager", "05/04/03")
mundo = Employee("Dr.Mundo Murdock", "Product Tester", "05/04/10")
poppy = Employee("Poppy Murdock", "Quality Control", "05/04/11")
olaf = Employee("Olaf Murdock", "Sales", "05/04/12")
cody = Employee("Cody Murdock", "Store Manager", "05/04/03")

# Assign 2 people to be employees of the first company.

store.hire(cody)
store.hire(olaf)

# Assign 3 people to be employees of the second company.

warehouse.hire(ashley)
warehouse.hire(mundo)
warehouse.hire(poppy)

# Output a report to the terminal the displays a business name, and its employees.
#For example:
"""
Acme Explosives is in the chemical industry and has the following employees
   * Michael Chang
   * Martina Navritilova

Jetways is in the transportation industry and has the following employees
   * Serena Williams
   * Roger Federer
   * Pete Sampras
"""
store.report()
print("\n")
warehouse.report()