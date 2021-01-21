

class Toys:
    def __init__(self, toy, price, quantity):
        self.toy = toy
        self.price = price
        self.quantity = quantity

t1 = Toys("Car", "$20", 100)
t2 = Toys("Box", "$5", 100)

toylist = str(t1.toy) + ' ' + str(t2.toy)
 
print(toylist)
