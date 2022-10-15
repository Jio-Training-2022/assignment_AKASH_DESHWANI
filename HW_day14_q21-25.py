# Write a class to represent a Laptop.

class Laptop:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.battery = 0
        self.power = 0

    def power_on(self):
        self.battery -= 1
        self.power += 1

    def charge_battery(self):
        self.battery += 20
        