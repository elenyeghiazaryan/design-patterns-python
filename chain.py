''' This example shows a Chain of Responsibility pattern for handling customer complaints.
Complaints go through different handlers: Cashier, Manager, and Customer Service.
Each handler tries to solve the complaint based on its type.
If the handler can't solve it, the complaint is passed to the next handler and if no one can solve it,
the complaint is not resolved.'''
class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, complaint_type):
        if self.next_handler:
            return self.next_handler.handle(complaint_type)
        return "Complaint not resolved."

class Cashier(Handler):
    def handle(self, complaint_type):
        if complaint_type == "payment":
            return "Cashier solved the payment issue."
        print("Cashier passed the complaint.")
        return super().handle(complaint_type)

class Manager(Handler):
    def handle(self, complaint_type):
        if complaint_type == "product":
            return "Manager solved the product issue."
        print("Manager passed the complaint.")
        return super().handle(complaint_type)

class CustomerService(Handler):
    def handle(self, complaint_type):
        if complaint_type == "delivery":
            return "Customer Service solved the delivery issue."
        return "Complaint not resolved."

# Createing chain
service = CustomerService()
manager = Manager(service)
cashier = Cashier(manager)

# Test complaints
print(cashier.handle("payment"))
print(cashier.handle("product"))
print(cashier.handle("delivery"))
print(cashier.handle("other"))
