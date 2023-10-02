class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")


class ThreeSeriews(BMW):

    def __init__(self, make, model, year, cruisecontrol):
        BMW.__init__(self, make, model, year)
        self.cruisecontrol = cruisecontrol


class FiveSeriews(BMW):

    def __init__(self, make, model, year, parkingcontrol):
        BMW.__init__(self, make, model, year)
        self.parkingcontrol = parkingcontrol


threeSeriews = ThreeSeriews(True, "BMW", 2003, True)
print(threeSeriews.year)
