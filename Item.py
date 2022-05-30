class Item(object):
    name = ''
    price: int
    rating: int

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating
