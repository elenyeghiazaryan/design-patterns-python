import abc
# Abstract Product
class Ticket(abc.ABC):
    @abc.abstractmethod
    def book(self):
        pass
# Abstract Product
class Snack(abc.ABC):
    @abc.abstractmethod
    def serve(self):
        pass
# Concrete Product
class BusTicket(Ticket):
    def book(self):
        print("Bus ticket booked.")

class TrainTicket(Ticket):
    def book(self):
        print("Train ticket booked.")

class FlightTicket(Ticket):
    def book(self):
        print("Flight ticket booked.")

# Concrete Product
class BusSnack(Snack):
    def serve(self):
        print("Sandwich for bus trip.")

class TrainSnack(Snack):
    def serve(self):
        print("Coffee for train trip.")

class FlightSnack(Snack):
    def serve(self):
        print("Tea for flight trip.")

# Abstract Factory
class TravelFactory(abc.ABC):
    @abc.abstractmethod
    def get_ticket(self):
        pass

    @abc.abstractmethod
    def get_snack(self):
        pass

# Concrete Factories
class BusFactory(TravelFactory):
    def get_ticket(self):
        return BusTicket()
    
    def get_snack(self):
        return BusSnack()

class TrainFactory(TravelFactory):
    def get_ticket(self):
        return TrainTicket()
    
    def get_snack(self):
        return TrainSnack()

class FlightFactory(TravelFactory):
    def get_ticket(self):
        return FlightTicket()
    
    def get_snack(self):
        return FlightSnack()

# for a client
def travel(factory):
    ticket = factory.get_ticket()
    snack = factory.get_snack()

    ticket.book()
    snack.serve()

if __name__ == "__main__":
    print("Bus Trip:")
    travel(BusFactory())

    print("\nTrain Trip:")
    travel(TrainFactory())

    print("\nFlight Trip:")
    travel(FlightFactory())
