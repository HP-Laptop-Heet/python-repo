# returning the value from the private function and get excess

class Order:
    def __init__(self,cart,customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return (len(self.cart))

order = Order(["banana","apple","mango"],"Real")
print(len(order))     # order is an object is used