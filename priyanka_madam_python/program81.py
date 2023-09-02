#  doubt

class Order:
    def __init__(self,cart,customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return (len(self.cart))

    def __add__(self):
        return (len(self.customer))

order = Order(["banana","apple","mango"],"Real")
print(len(order))