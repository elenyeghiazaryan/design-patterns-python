# 1) 
class Vacation:
    def __init__(self):
        self.plan = []

    def add(self, item):
        self.plan.append(item)

    def show(self):
        print("The vacation Plan Includes:")
        for item in self.plan:
            print(" -", item)

class VacationBuilder:
    def __init__(self):
        self.vacation = Vacation()

    def add_flight(self):
        self.vacation.add("Round-trip Flight")
        return self

    def add_hotel(self):
        self.vacation.add("5-Star Hotel")
        return self

    def add_meals(self):
        self.vacation.add("All-Inclusive Meals")
        return self

    def add_tour(self):
        self.vacation.add("City Tour")
        return self
    
    def build(self):
        return self.vacation

builder = VacationBuilder()
trip = (
    builder
    .add_flight()
    .add_hotel()
    .add_meals()
    .add_tour()

    .build()
)
trip.show()


#2)
from abc import ABC, abstractmethod

# 1. Product
class Vacation:
    def __init__(self):
        self.plan = []

    def add(self, item):
        self.plan.append(item)

    def show(self):
        print("Vacation Plan:")
        for item in self.plan:
            print(" -", item)


#Abstract Builder
class VacationBuilder(ABC):
    def __init__(self):
        self.vacation = Vacation()

    @abstractmethod
    def book_transport(self): pass

    @abstractmethod
    def book_hotel(self): pass

    @abstractmethod
    def add_activity(self): pass

    def get_result(self):
        return self.vacation


#Concrete Builder 
class BeachVacationBuilder(VacationBuilder):
    def book_transport(self):
        self.vacation.add("Flight to Maldives")

    def book_hotel(self):
        self.vacation.add("Bungalow Resort")

    def add_activity(self):
        self.vacation.add("Diving")

class MountainVacationBuilder(VacationBuilder):
    def book_transport(self):
        self.vacation.add("Train to Swiss Alps")

    def book_hotel(self):
        self.vacation.add("Cozy Mountains")

    def add_activity(self):
        self.vacation.add("Hiking")

class TravelPlanner:
    def __init__(self, builder: VacationBuilder):
        self.builder = builder

    def build_vacation(self):
        self.builder.book_transport()
        self.builder.book_hotel()
        self.builder.add_activity()
        return self.builder.get_result()

beach_builder = BeachVacationBuilder()
planner = TravelPlanner(beach_builder)
beach_trip = planner.build_vacation()
beach_trip.show()

print("\n")
mountain_builder = MountainVacationBuilder()
planner = TravelPlanner(mountain_builder)
mountain_trip = planner.build_vacation()
mountain_trip.show()


