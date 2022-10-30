class Human:
    def __init__(self, name = "Human"):
        self.name = name


class Car:
    def __init__(self, brand):
        self.brand=brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)
    def print_passenger_name(self):
        if self.passengers != []:
            print(f"Names of {self.brand}, Passengers ")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers for now in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
car = Car("Voltswagen")
car.add_passenger(nick)
car.add_passenger(kate)
car.print_passenger_name()






