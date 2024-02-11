-- object-oriented programming allows you to create large, modular programs that can easily expand over time;
-- object-oriented programs hide the implementation from the end-user.

**Class**
-- Imagine that you in a clothes store and want buy a shirt, then the operations and description of the shirt can shown as:

class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price): #self >> differentiate between objects 
        #all shirt characteristic
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price): #method can be done on shirt
        self.price = new_price

    def discount(self, discount):
        return self.price * (1-discount)

new_shirt = Shirt('red', 'S', 'short sleeve', 15) #add new shirt

print(new_shirt.color)    #to print any characteristic
print(new_shirt.style)
print(new_shirt.price)
print(new_shirt.discount(.2))

tshirt_collection = []    #create an empty list and fill it with these inputs by append
shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve', 10)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three )

for i in range(len(tshirt_collection)):
   print (tshirt_collection[i].color)    #print all tshirts colors










