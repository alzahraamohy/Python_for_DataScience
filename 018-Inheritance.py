-- Imagine that you are in a clothing shop and want to describe ( pants, skirts, dresses, socks ) and the following methods
   change_price, discount_price
    they all have the same attributes (color, size, style, etc), it is hard to make each one a class and describe that it has these attributes.
      instead, we use inheritance to inherit them from a parent class called clothing, and( pants, skirts, dresses, socks ) called children.

-- Anytime we want to add an attribute we will add it to the parent, instead of adding it to each class.

**Example**
class Clothing:
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price

    def calculate_discount(self, discount):
        return self.price * (1 - discount)

class Shirt(Clothing):
    def __init__(self, color, size, style, price, long_or_short):
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short

    def double_price(self):
        self.price = 2*self.price

class Pants(Clothing):
    def __init__(self, color, size, style, price, waist):
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)




