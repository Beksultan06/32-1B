

from models.base import BaseModel
from datetime import datetime

class Order(BaseModel):
    orders = []

    def __init__(self, id, customer, products : list):
        super().__init__(id)
        self.customer = customer
        self.products = products
        self.date = datetime.now()

    def total_price(self):
        return sum(p.price for p in self.products)

    def save(self):
        Order.orders.append(self)

    @classmethod
    def total_orders(cls):
        return len(cls.orders)

    def __repr__(self):
        return f"Order #{self.id} от {self.customer.name}"