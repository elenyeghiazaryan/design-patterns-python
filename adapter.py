'''The Tesla has a different charging method, so we use an adapter
allowing Tesla charge using a standard charger. '''
class CarCharger:
    def charge(self):
        pass

class Tesla: # Tesla with a tifferent method
    def plug_in_tesla(self):
        print("Tesla is now charging through Tesla plug.")

class TeslaAdapter(CarCharger): # Adapter for Tesla with standard charger
    def __init__(self, tesla):
        self.tesla = tesla

    def charge(self):
        self.tesla.plug_in_tesla()

def start_charging(car):
    car.charge()

my_tesla = Tesla()
adapted_tesla = TeslaAdapter(my_tesla)

start_charging(adapted_tesla)
