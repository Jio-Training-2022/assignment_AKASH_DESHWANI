# Write a class to represent a car 

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0
        self.gas = 0
    
    def drive(self):
        self.mileage += 10
        self.gas -= 1
    
    def fill_gas(self):
        self.gas += 20

# Write a class to represent an ATM machine.
class ATM:
    def __init__(self, bank, location):
        self.bank = bank
        self.location = location
        self.balance = 0
        self.withdraw = 0
        self.deposit = 0
    
    def withdraw(self):
        self.balance -= 100
        self.withdraw += 1
    
    def deposit(self):
        self.balance += 100
        self.deposit += 1




# Write a class to represent a school.

class school:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.students = 0
        self.teachers = 0
    
    def enroll(self):
        self.students += 1
    
    def hire(self):
        self.teachers += 1



# Write a class to represent a company. 

class company:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = 0
        self.revenue = 0
    
    def hire(self):
        self.employees += 1
    
    def generate_revenue(self):
        self.revenue += 1000


# Write a class to represent a Journey / Trip. 

class trip:
    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance
        self.miles = 0
        self.gas = 0
    
    def drive(self):
        self.miles += 10
        self.gas -= 1
    
    def fill_gas(self):
        self.gas += 20
