import abc
# 1. Abstract Product
class Ticket(abc.ABC):
    def __init__(self, name, dest):
        self.name = name
        self.dest = dest

    @abc.abstractmethod
    def book(self):
        pass

# 2. Concrete Products
class BusTicket(Ticket):
    def book(self):
        print(f"Bus ticket for {self.name} to {self.dest} booked.")

class TrainTicket(Ticket):
    def book(self):
        print(f"Train ticket for {self.name} to {self.dest} booked.")

class FlightTicket(Ticket):
    def book(self):
        print(f"Flight ticket for {self.name} to {self.dest} booked.")

# 3. Factory
class TicketCreator(abc.ABC):
    @abc.abstractmethod
    def create(self, name, dest):
        pass

    def book_ticket(self, name, dest):
        ticket = self.create(name, dest)
        ticket.book()

# 4. Concrete Creators
class BusCreator(TicketCreator):
    def create(self, name, dest):
        return BusTicket(name, dest)

class TrainCreator(TicketCreator):
    def create(self, name, dest):
        return TrainTicket(name, dest)

class FlightCreator(TicketCreator):
    def create(self, name, dest):
        return FlightTicket(name, dest)

# Client
if __name__ == "__main__":
    orders = [
        (BusCreator(), "Lia",  "Arshakunyanc"),
        (TrainCreator(), "Elen", "Gyumri"),
        (FlightCreator(), "Lucy", "Milan"),
    ]
    for creator, name, dest in orders:
        creator.book_ticket(name, dest)
