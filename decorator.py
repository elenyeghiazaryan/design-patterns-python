'''Decorator pattern: creating a bouquet by adding flowers and decorations, 
each addition adds to the price and description without changing the original.'''

class Bouquet:
    def cost(self):
        return 20  # Base bouquet price
    def description(self):
        return "Plain bouquet"

class BouquetAddon:
    def __init__(self, bouquet):
        self.bouquet = bouquet

    def cost(self):
        return self.bouquet.cost()

    def description(self):
        return self.bouquet.description()
    
class Daisies(BouquetAddon): # For adding daisies
    def cost(self):
        return self.bouquet.cost() + 5

    def description(self):
        return self.bouquet.description() + ", Daisies"

class Lilies(BouquetAddon): # For adding lilies
    def cost(self):
        return self.bouquet.cost() + 5

    def description(self):
        return self.bouquet.description() + ", Lilies"

class Tulips(BouquetAddon): # For adding tulips
    def cost(self):
        return self.bouquet.cost() + 7

    def description(self):
        return self.bouquet.description() + ", Tulips"

class Roses(BouquetAddon): # For adding roses
    def cost(self):
        return self.bouquet.cost() + 10

    def description(self):
        return self.bouquet.description() + ", Roses"

class Peonies(BouquetAddon): # For adding Peonies
    def cost(self):
        return self.bouquet.cost() + 15

    def description(self):
        return self.bouquet.description() + ", Peonies"
    
class Decoration(BouquetAddon):
    def cost(self):
        return self.bouquet.cost() + 3

    def description(self):
        return self.bouquet.description() + ", Decoration"

# Create a bouquet with peonies and +decoration
bouquet1 = Bouquet()
bouquet1 = Peonies(bouquet1)
bouquet1 = Decoration(bouquet1)
print(bouquet1.description())
print("Total price:", bouquet1.cost())

# Creating a bouquet with roses only
bouquet2 = Bouquet()
bouquet2 = Roses(bouquet2)
print(bouquet2.description())
print("Total price:", bouquet2.cost())
print()

# Creating a bouquet with lilies and daises
bouquet3 = Bouquet()
bouquet3 = Lilies(bouquet3)
bouquet3 = Daisies(bouquet3)
print(bouquet3.description())
print("Total price:", bouquet3.cost())
print()